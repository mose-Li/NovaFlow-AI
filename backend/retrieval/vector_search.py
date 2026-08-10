import json
import math

from backend.embedding.embedding_service import EmbeddingService
from backend.repositories.embedding_repository import EmbeddingRepository


class VectorSearch:

    def __init__(self):

        self.embedder = EmbeddingService()

        self.repository = EmbeddingRepository()

    def cosine_similarity(
        self,
        vector1,
        vector2,
    ):

        dot = sum(a * b for a, b in zip(vector1, vector2))

        norm1 = math.sqrt(sum(a * a for a in vector1))

        norm2 = math.sqrt(sum(b * b for b in vector2))

        if norm1 == 0 or norm2 == 0:
            return 0.0

        return dot / (norm1 * norm2)

    def search(
        self,
        question,
        top_k=3,
    ):

        query_vector = self.embedder.encode(question)

        rows = self.repository.list_embeddings()

        scores = []

        for row in rows:

            embedding = json.loads(row[3])

            similarity = self.cosine_similarity(
                query_vector,
                embedding,
            )

            scores.append(
                {
                    "chunk_id": row[1],
                    "score": similarity,
                }
            )

        scores.sort(
            key=lambda x: x["score"],
            reverse=True,
        )

        return scores[:top_k]