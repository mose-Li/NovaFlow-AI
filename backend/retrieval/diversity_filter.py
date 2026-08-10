class DiversityFilter:
    """
    Ensure search results are diversified across documents.
    """

    @staticmethod
    def diversify(results, max_chunks_per_document=2):

        document_counter = {}
        diversified = []

        for item in results:

            document_id = item["document_id"]

            count = document_counter.get(document_id, 0)

            if count >= max_chunks_per_document:
                continue

            diversified.append(item)

            document_counter[document_id] = count + 1

        return diversified