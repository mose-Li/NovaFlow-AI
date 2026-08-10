from pathlib import Path

from backend.chunk.chunk_service import ChunkService
from backend.embedding.embedding_service import EmbeddingService
from backend.parser.parser_factory import ParserFactory
from backend.repositories.document_repository import DocumentRepository
from backend.repositories.embedding_repository import EmbeddingRepository
from backend.utils.file_utils import (
    calculate_sha256,
    generate_filename,
    validate_extension,
)


class DocumentService:

    def __init__(self):

        self.repository = DocumentRepository()
        self.embedding_repository = EmbeddingRepository()

        self.chunk_service = ChunkService()
        self.embedding_service = EmbeddingService()

    # ==========================
    # 上传文档
    # ==========================
    def upload_document(
        self,
        original_filename: str,
        mime_type: str,
        file_bytes: bytes,
    ):

        # 文件类型验证
        file_type = validate_extension(original_filename)

        file_size = len(file_bytes)

        checksum = calculate_sha256(file_bytes)

        # 是否重复
        exists = self.repository.get_by_checksum(checksum)

        if exists:
            raise ValueError("Document already exists.")

        # UUID文件名
        stored_filename = generate_filename(original_filename)

        save_path = Path("uploads") / stored_filename

        save_path.parent.mkdir(parents=True, exist_ok=True)

        with open(save_path, "wb") as f:
            f.write(file_bytes)

        # 保存 documents
        document_id = self.repository.create_document(
            original_filename=original_filename,
            stored_filename=stored_filename,
            file_type=file_type,
            mime_type=mime_type,
            file_size=file_size,
            checksum=checksum,
        )

        # ==========================
        # Parser
        # ==========================
        parser = ParserFactory.get_parser(file_type)

        content = parser.parse(str(save_path))

        # ==========================
        # 保存全文
        # ==========================
        self.repository.save_document_content(
            document_id=document_id,
            content=content,
            page_count=1,
            word_count=len(content),
        )

        # ==========================
        # Chunk（新版）
        # ==========================
        chunks = self.chunk_service.split(content)

        for index, chunk in enumerate(chunks):

            chunk_id = self.repository.save_chunk(
                document_id=document_id,
                chunk_index=index,
                content=chunk,
                token_count=len(chunk.split()),
            )

            # ==========================
            # Embedding
            # ==========================
            vector = self.embedding_service.encode(chunk)

            self.embedding_repository.save_embedding(
                chunk_id=chunk_id,
                model_name=self.embedding_service.model_name,
                embedding=vector,
                dimension=len(vector),
            )

        return {
            "document_id": document_id,
            "filename": original_filename,
            "stored_filename": stored_filename,
            "file_size": file_size,
            "status": "READY",
            "chunks": len(chunks),
            "embeddings": len(chunks),
        }

    # ==========================
    # 查询全部文档
    # ==========================
    def list_documents(self):

        rows = self.repository.list_documents()

        result = []

        for row in rows:

            result.append(
                {
                    "id": row[0],
                    "filename": row[1],
                    "stored_filename": row[2],
                    "file_type": row[3],
                    "mime_type": row[4],
                    "file_size": row[5],
                    "checksum": row[6],
                    "upload_time": row[7],
                    "status": row[8],
                }
            )

        return result

    # ==========================
    # 删除文档
    # ==========================
    def delete_document(self, document_id: int):

        row = self.repository.get_document(document_id)

        if not row:
            raise ValueError("Document not found.")

        file_path = Path("uploads") / row[2]

        if file_path.exists():
            file_path.unlink()

        self.repository.delete_document(document_id)

        return {
            "message": "Document deleted successfully."
        }