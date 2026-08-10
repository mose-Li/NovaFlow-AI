from sqlalchemy import create_engine, text

from config.settings import settings


class DocumentRepository:

    def __init__(self):
        self.engine = create_engine(settings.DATABASE_URL)

    # ==========================
    # Documents
    # ==========================

    def create_document(
        self,
        original_filename,
        stored_filename,
        file_type,
        mime_type,
        file_size,
        checksum,
    ):

        with self.engine.begin() as conn:

            result = conn.execute(
                text("""
                    INSERT INTO documents
                    (
                        original_filename,
                        stored_filename,
                        file_type,
                        mime_type,
                        file_size,
                        checksum
                    )
                    VALUES
                    (
                        :original_filename,
                        :stored_filename,
                        :file_type,
                        :mime_type,
                        :file_size,
                        :checksum
                    )
                """),
                {
                    "original_filename": original_filename,
                    "stored_filename": stored_filename,
                    "file_type": file_type,
                    "mime_type": mime_type,
                    "file_size": file_size,
                    "checksum": checksum,
                },
            )

            return result.lastrowid

    def get_document(self, document_id):

        with self.engine.connect() as conn:

            result = conn.execute(
                text("""
                    SELECT *
                    FROM documents
                    WHERE id = :id
                """),
                {
                    "id": document_id
                },
            )

            return result.fetchone()

    def get_by_checksum(self, checksum):

        with self.engine.connect() as conn:

            result = conn.execute(
                text("""
                    SELECT *
                    FROM documents
                    WHERE checksum = :checksum
                """),
                {
                    "checksum": checksum
                },
            )

            return result.fetchone()

    def list_documents(self):

        with self.engine.connect() as conn:

            result = conn.execute(
                text("""
                    SELECT *
                    FROM documents
                    ORDER BY id DESC
                """)
            )

            return result.fetchall()

    def delete_document(self, document_id):

        with self.engine.begin() as conn:

            result = conn.execute(
                text("""
                    DELETE FROM documents
                    WHERE id = :id
                """),
                {
                    "id": document_id
                },
            )

            return result.rowcount

    # ==========================
    # Document Contents
    # ==========================

    def save_document_content(
        self,
        document_id,
        content,
        page_count,
        word_count,
    ):

        with self.engine.begin() as conn:

            conn.execute(
                text("""
                    INSERT INTO document_contents
                    (
                        document_id,
                        content,
                        page_count,
                        word_count
                    )
                    VALUES
                    (
                        :document_id,
                        :content,
                        :page_count,
                        :word_count
                    )
                """),
                {
                    "document_id": document_id,
                    "content": content,
                    "page_count": page_count,
                    "word_count": word_count,
                },
            )

    def get_document_content(self, document_id):

        with self.engine.connect() as conn:

            result = conn.execute(
                text("""
                    SELECT *
                    FROM document_contents
                    WHERE document_id = :id
                """),
                {
                    "id": document_id
                },
            )

            return result.fetchone()

    # ==========================
    # Chunks
    # ==========================

    def save_chunk(
        self,
        document_id,
        chunk_index,
        content,
        token_count,
    ):

        with self.engine.begin() as conn:

            result = conn.execute(
                text("""
                    INSERT INTO document_chunks
                    (
                        document_id,
                        chunk_index,
                        content,
                        token_count
                    )
                    VALUES
                    (
                        :document_id,
                        :chunk_index,
                        :content,
                        :token_count
                    )
                """),
                {
                    "document_id": document_id,
                    "chunk_index": chunk_index,
                    "content": content,
                    "token_count": token_count,
                },
            )

            return result.lastrowid

    def list_chunks(self, document_id):

        with self.engine.connect() as conn:

            result = conn.execute(
                text("""
                    SELECT *
                    FROM document_chunks
                    WHERE document_id = :id
                    ORDER BY chunk_index
                """),
                {
                    "id": document_id
                },
            )

            return result.fetchall()

    def get_chunk(self, chunk_id):

        with self.engine.connect() as conn:

            result = conn.execute(
                text("""
                    SELECT *
                    FROM document_chunks
                    WHERE id = :id
                """),
                {
                    "id": chunk_id
                },
            )

            return result.fetchone()

    def list_all_chunks(self):

        with self.engine.connect() as conn:

            result = conn.execute(
                text("""
                    SELECT *
                    FROM document_chunks
                    ORDER BY id
                """)
            )

            return result.fetchall()
    def get_chunk_with_document(self, chunk_id):

        with self.engine.connect() as conn:

            result = conn.execute(
                text("""
                    SELECT
                        c.id,
                        c.document_id,
                        c.chunk_index,
                        c.content,
                        d.original_filename
                    FROM document_chunks c
                    JOIN documents d
                      ON c.document_id = d.id
                    WHERE c.id = :id
                """),
                {
                    "id": chunk_id
                },
            )

            return result.fetchone()