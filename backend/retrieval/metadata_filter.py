class MetadataFilter:
    """
    Enterprise Metadata Filter

    Supported metadata (future):

    - language
    - department
    - category
    - author
    - tags
    - document_type
    """

    @staticmethod
    def filter(results, metadata=None):

        if metadata is None:
            metadata = {}

        if not metadata:
            return results

        filtered = []

        for item in results:

            matched = True

            for key, value in metadata.items():

                if item.get(key) != value:

                    matched = False
                    break

            if matched:
                filtered.append(item)

        return filtered