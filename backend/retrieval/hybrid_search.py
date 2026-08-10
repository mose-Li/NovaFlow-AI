from backend.rag.vector_search import VectorSearch
from backend.retrieval.bm25_search import BM25Search

from backend.retrieval.retrieval_config import RetrievalConfig
from backend.retrieval.score_fusion import ScoreFusion
from backend.retrieval.score_filter import ScoreFilter
from backend.retrieval.score_normalizer import ScoreNormalizer
from backend.retrieval.metadata_filter import MetadataFilter
from backend.retrieval.diversity_filter import DiversityFilter
from backend.retrieval.dynamic_topk import DynamicTopK


class HybridSearch:
    """
    Enterprise Hybrid Retrieval

    Pipeline:

        Vector Search
              +
        BM25 Search
              ↓
        Score Normalization
              ↓
        Weighted Score Fusion
              ↓
        Score Filtering
              ↓
        Metadata Filter
              ↓
        Diversity Filter
              ↓
        Dynamic Top-K
              ↓
        Ranking
              ↓
        Final Results
    """

    def __init__(self):

        self.vector_search = VectorSearch()
        self.bm25_search = BM25Search()

    # ==================================================
    # Hybrid Search
    # ==================================================
    def search(
        self,
        query: str,
        top_k: int = None,
        vector_top_k: int = None,
        bm25_top_k: int = None,
    ):

        # ------------------------------------------
        # Load Configuration
        # ------------------------------------------

        if top_k is None:
            top_k = RetrievalConfig.FINAL_TOP_K

        if vector_top_k is None:
            vector_top_k = RetrievalConfig.VECTOR_TOP_K

        if bm25_top_k is None:
            bm25_top_k = RetrievalConfig.BM25_TOP_K

        # ------------------------------------------
        # Vector Search
        # ------------------------------------------

        vector_results = self.vector_search.search(
            query=query,
            top_k=vector_top_k,
        )

        # ------------------------------------------
        # BM25 Search
        # ------------------------------------------

        bm25_results = self.bm25_search.search(
            query=query,
            top_k=bm25_top_k,
        )

        merged = {}

        # ------------------------------------------
        # Merge Vector Results
        # ------------------------------------------

        for item in vector_results:

            chunk_id = item["chunk_id"]

            merged[chunk_id] = {
                "chunk_id": item["chunk_id"],
                "document_id": item["document_id"],
                "chunk_index": item["chunk_index"],
                "content": item["content"],
                "vector_score": item["score"],
                "bm25_score": 0.0,
            }

        # ------------------------------------------
        # Merge BM25 Results
        # ------------------------------------------

        for item in bm25_results:

            chunk_id = item["chunk_id"]

            if chunk_id in merged:

                merged[chunk_id]["bm25_score"] = item["score"]

            else:

                merged[chunk_id] = {
                    "chunk_id": item["chunk_id"],
                    "document_id": item["document_id"],
                    "chunk_index": item["chunk_index"],
                    "content": item["content"],
                    "vector_score": 0.0,
                    "bm25_score": item["score"],
                }

        # ------------------------------------------
        # Convert to List
        # ------------------------------------------

        results = list(merged.values())

        if not results:
            return []

        # ------------------------------------------
        # Normalize Scores
        # ------------------------------------------

        vector_scores = [
            item["vector_score"]
            for item in results
        ]

        bm25_scores = [
            item["bm25_score"]
            for item in results
        ]

        normalized_vector = ScoreNormalizer.min_max(
            vector_scores
        )

        normalized_bm25 = ScoreNormalizer.min_max(
            bm25_scores
        )

        # ------------------------------------------
        # Hybrid Score
        # ------------------------------------------

        for i in range(len(results)):

            results[i]["vector_score"] = normalized_vector[i]

            results[i]["bm25_score"] = normalized_bm25[i]

            results[i]["hybrid_score"] = ScoreFusion.weighted_sum(
                vector_score=results[i]["vector_score"],
                bm25_score=results[i]["bm25_score"],
                vector_weight=RetrievalConfig.VECTOR_WEIGHT,
                bm25_weight=RetrievalConfig.BM25_WEIGHT,
            )

        # ------------------------------------------
        # Score Threshold Filter
        # ------------------------------------------

        results = ScoreFilter.filter_results(
            results=results,
            min_score=RetrievalConfig.MIN_HYBRID_SCORE,
        )

        # ------------------------------------------
        # Metadata Filter
        # ------------------------------------------

        results = MetadataFilter.filter(
            results=results,
            metadata={},
        )

        # ------------------------------------------
        # Diversity Filter
        # ------------------------------------------

        results = DiversityFilter.diversify(
            results=results,
            max_chunks_per_document=RetrievalConfig.MAX_CHUNKS_PER_DOCUMENT,
        )

        # ------------------------------------------
        # Ranking
        # ------------------------------------------

        results.sort(
            key=lambda x: x["hybrid_score"],
            reverse=True,
        )

        # ------------------------------------------
        # Dynamic Top-K
        # ------------------------------------------

        results = DynamicTopK.select(
            results=results,
            min_score=RetrievalConfig.DYNAMIC_TOP_K_MIN_SCORE,
            max_top_k=min(
                top_k,
                RetrievalConfig.DYNAMIC_TOP_K_MAX,
            ),
        )

        return results