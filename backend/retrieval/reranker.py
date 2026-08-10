"""
Enterprise Cross-Encoder Reranker

Re-ranks hybrid retrieval results using a CrossEncoder model.

Version:
    v0.5.0
"""

from sentence_transformers import CrossEncoder


class Reranker:
    """
    Enterprise Cross-Encoder Reranker.
    """

    def __init__(
        self,
        model_name: str = "BAAI/bge-reranker-base",
    ) -> None:

        self.model = CrossEncoder(model_name)

    # ==================================================
    # Step 1: Rerank Retrieved Results
    # ==================================================
    def rerank(
        self,
        query: str,
        candidates: list,
        top_k: int = 5,
    ) -> list[dict]:

        if not query.strip():
            return []

        if not candidates:
            return []

        sentence_pairs = []

        for item in candidates:

            content = item.get("content", "")

            sentence_pairs.append(
                (
                    query,
                    content,
                )
            )

        scores = self.model.predict(sentence_pairs)

        if scores is None:
            return []

        results = []

        for item, score in zip(candidates, scores):

            new_item = item.copy()

            new_item["rerank_score"] = float(score)

            results.append(new_item)

        results.sort(
            key=lambda x: x["rerank_score"],
            reverse=True,
        )

        return results[:top_k]