"""
Result filtering.
"""


class ScoreFilter:

    @staticmethod
    def filter_results(
        results,
        min_score,
    ):

        filtered = []

        for item in results:

            if item["hybrid_score"] >= min_score:

                filtered.append(item)

        return filtered