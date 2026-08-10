"""
Enterprise Dense Vector Retrieval

Performs semantic retrieval using embedding vectors and cosine similarity.

Version:
    v0.5.0
"""

import json

import numpy as np

from backend.embedding.embedding_service import EmbeddingService
from backend.repositories.document_repository import DocumentRepository
from backend.repositories.embedding_repository import EmbeddingRepository


class VectorSearch:
    """
    Enterprise Dense Vector Retriever.
    """

    def __init__(self):

        self.embedding_service = EmbeddingService()
        self.embedding_repository = EmbeddingRepository()
        self.document_repository = DocumentRepository()

    # ==================================================
    # Step 1: Calculate Cosine Similarity
    # ==================================================
    @staticmethod
    def cosine_similarity(
        vec1,
        vec2,
    ) -> float:

        vec1 = np.array(vec1)
        vec2 = np.array(vec2)

        denominator = np.linalg.norm(vec1) * np.linalg.norm(vec2)

        if denominator == 0:
            return 0.0

        return float(np.dot(vec1, vec2) / denominator)

    # ==================================================
    # Step 2: Dense Vector Retrieval
    # ==================================================
    def search(
        self,
        query: str,
        top_k: int = 5,
        threshold: float = 0.30,
    ) -> list[dict]:

        # Empty query
        if not query.strip():
            return []

        # Encode query
        query_embedding = self.embedding_service.encode(query)

        results = []

        # Load all chunks
        all_chunks = self.document_repository.list_all_chunks()

        if not all_chunks:
            return []

        # Calculate similarity
        for chunk in all_chunks:

            chunk_id = chunk[0]

            embedding = self.embedding_repository.get_embedding(chunk_id)

            if embedding is None:
                continue

            vector = json.loads(embedding[3])

            score = self.cosine_similarity(
                query_embedding,
                vector,
            )

            results.append(
                {
                    "chunk_id": chunk_id,
                    "document_id": chunk[1],
                    "chunk_index": chunk[2],
                    "content": chunk[3],
                    "score": score,
                }
            )

        # Rank by similarity
        results.sort(
            key=lambda x: x["score"],
            reverse=True,
        )

        # ==================================================
        # Step 3: Similarity Threshold Filtering
        # ==================================================
        filtered_results = []

        for item in results:

            if item["score"] >= threshold:
                filtered_results.append(item)

        # ==================================================
        # Step 4: Dynamic Top-K
        # ==================================================
        if not filtered_results:
            return []

        if len(filtered_results) <= top_k:
            return filtered_results

        return filtered_results[:top_k]