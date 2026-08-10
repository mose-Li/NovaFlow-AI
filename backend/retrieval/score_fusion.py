"""
Hybrid score fusion strategies.
"""


class ScoreFusion:

    @staticmethod
    def weighted_sum(
        vector_score: float,
        bm25_score: float,
        vector_weight: float,
        bm25_weight: float,
    ) -> float:

        return (
            vector_score * vector_weight
            + bm25_score * bm25_weight
        )