class ContextDeduplicator:
    """
    Context 去重器
    """

    @staticmethod
    def deduplicate(contexts: list):

        seen = set()
        result = []

        for item in contexts:

            content = item["content"].strip()

            if content in seen:
                continue

            seen.add(content)
            result.append(item)

        return result