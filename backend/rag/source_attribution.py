class SourceAttribution:
    """
    Build source references for retrieved contexts.
    """

    @staticmethod
    def build(contexts):

        sources = []

        for item in contexts:

            sources.append(
                {
                    "document_id": item["document_id"],
                    "chunk_id": item["chunk_id"],
                    "chunk_index": item["chunk_index"],
                }
            )

        return sources