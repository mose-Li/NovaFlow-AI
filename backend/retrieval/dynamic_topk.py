class DynamicTopK:
    """
    Enterprise Dynamic Top-K Selector

    Select retrieval results dynamically according
    to hybrid scores.
    """

    @staticmethod
    def select(
        results,
        min_score=0.55,
        max_top_k=5,
    ):
        """
        Parameters
        ----------
        results : list
            Retrieval results sorted by hybrid_score.

        min_score : float
            Minimum hybrid score required.

        max_top_k : int
            Maximum number of returned chunks.
        """

        selected = []

        for item in results:

            if item["hybrid_score"] < min_score:
                continue

            selected.append(item)

            if len(selected) >= max_top_k:
                break

        return selected