import json

from sqlalchemy import create_engine, text

from config.settings import settings


class EmbeddingRepository:

    def __init__(self):
        self.engine = create_engine(settings.DATABASE_URL)

    # 保存Embedding
    def save_embedding(
        self,
        chunk_id,
        model_name,
        embedding,
        dimension,
    ):

        if isinstance(embedding, list):
            embedding = json.dumps(embedding)

        with self.engine.begin() as conn:

            result = conn.execute(
                text("""
                    INSERT INTO embeddings
                    (
                        chunk_id,
                        model_name,
                        embedding,
                        dimension
                    )
                    VALUES
                    (
                        :chunk_id,
                        :model_name,
                        :embedding,
                        :dimension
                    )
                """),
                {
                    "chunk_id": chunk_id,
                    "model_name": model_name,
                    "embedding": embedding,
                    "dimension": dimension,
                },
            )

            return result.lastrowid

    # 查询一个Chunk对应Embedding
    def get_embedding(self, chunk_id):

        with self.engine.connect() as conn:

            result = conn.execute(
                text("""
                    SELECT *
                    FROM embeddings
                    WHERE chunk_id = :chunk_id
                """),
                {
                    "chunk_id": chunk_id
                },
            )

            return result.fetchone()

    # 查询全部Embedding
    def list_embeddings(self):

        with self.engine.connect() as conn:

            result = conn.execute(
                text("""
                    SELECT *
                    FROM embeddings
                    ORDER BY id
                """)
            )

            return result.fetchall()

    # 删除一个Chunk对应Embedding
    def delete_embedding(self, chunk_id):

        with self.engine.begin() as conn:

            result = conn.execute(
                text("""
                    DELETE FROM embeddings
                    WHERE chunk_id = :chunk_id
                """),
                {
                    "chunk_id": chunk_id
                }
            )

            return result.rowcount

    # 删除一个Document的全部Embedding
    def delete_document_embeddings(self, document_id):

        with self.engine.begin() as conn:

            result = conn.execute(
                text("""
                    DELETE FROM embeddings
                    WHERE chunk_id IN
                    (
                        SELECT id
                        FROM document_chunks
                        WHERE document_id = :document_id
                    )
                """),
                {
                    "document_id": document_id
                }
            )

            return result.rowcount