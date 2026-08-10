class ScoreNormalizer:
    """
    Normalize retrieval scores.

    Supported methods:

    - Min-Max Normalization
    """

    @staticmethod
    def min_max(scores):

        if not scores:
            return []

        minimum = min(scores)
        maximum = max(scores)

        if maximum == minimum:
            return [1.0 for _ in scores]

        return [
            (s - minimum) / (maximum - minimum)
            for s in scores
        ]