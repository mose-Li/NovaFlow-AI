import re


class ContextCleaner:
    """
    Context 清洗器

    功能：
    1. 去除首尾空白
    2. 合并连续空行
    3. 去除每行首尾空格
    4. 删除空 Context
    """

    @staticmethod
    def clean(text: str) -> str:

        if not text:
            return ""

        # 去掉首尾空白
        text = text.strip()

        # 去掉每一行首尾空格
        lines = [line.strip() for line in text.splitlines()]

        # 删除空行
        cleaned_lines = []

        previous_blank = False

        for line in lines:

            if line == "":

                if previous_blank:
                    continue

                previous_blank = True
                cleaned_lines.append("")
            else:
                previous_blank = False
                cleaned_lines.append(line)

        text = "\n".join(cleaned_lines)

        # 连续三个以上空行压缩成两个
        text = re.sub(r"\n{3,}", "\n\n", text)

        return text.strip()

    @classmethod
    def clean_contexts(cls, contexts: list):

        result = []

        for item in contexts:

            content = cls.clean(item["content"])

            if content == "":
                continue

            new_item = item.copy()
            new_item["content"] = content

            result.append(new_item)

        return result