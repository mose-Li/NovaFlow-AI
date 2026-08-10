class SmartMerge:

    @staticmethod
    def merge(paragraphs):

        merged = []

        i = 0

        while i < len(paragraphs):

            current = paragraphs[i].strip()

            # 空行
            if not current:
                i += 1
                continue

            # 判断是不是标题
            is_title = (
                len(current) <= 20
                or current.endswith("：")
                or current.endswith(":")
                or current.endswith("#")
            )

            # 如果下一段存在
            if is_title and i + 1 < len(paragraphs):

                merged.append(
                    current + "\n" + paragraphs[i + 1].strip()
                )

                i += 2

            else:

                merged.append(current)

                i += 1

        return merged