import re


class SemanticChunk:

    # ==========================
    # 判断是否标题
    # ==========================
    @staticmethod
    def is_heading(text: str):

        text = text.strip()

        if not text:
            return False

        # 以冒号结尾
        if text.endswith("：") or text.endswith(":"):
            return True

        # Markdown 标题
        if text.startswith("#"):
            return True

        # 一、 二、 三、
        if re.match(r"^[一二三四五六七八九十]+、", text):
            return True

        # 1.
        if re.match(r"^\d+\.", text):
            return True

        # 1)
        if re.match(r"^\d+\)", text):
            return True

        # （一）
        if re.match(r"^（[一二三四五六七八九十]+）", text):
            return True

        return False

    # ==========================
    # 构建 Section
    # ==========================
    @classmethod
    def build_sections(cls, paragraphs):

        sections = []
        current = []

        for paragraph in paragraphs:

            paragraph = paragraph.strip()

            if not paragraph:
                continue

            # 遇到标题，开启新的 Section
            if cls.is_heading(paragraph):

                if current:
                    sections.append("\n".join(current))

                current = [paragraph]

            else:

                current.append(paragraph)

        if current:
            sections.append("\n".join(current))

        return sections

    # ==========================
    # 超长 Section 自动切分
    # 按段落切，不从一句话中间截断
    # ==========================
    @classmethod
    def split_large_sections(
        cls,
        sections,
        chunk_size=500,
    ):

        results = []

        for section in sections:

            # 不超长，直接保留
            if len(section) <= chunk_size:
                results.append(section)
                continue

            paragraphs = section.split("\n")

            current = ""

            for p in paragraphs:

                p = p.strip()

                if not p:
                    continue

                # 当前 Chunk 还能放下
                if len(current) + len(p) + 1 <= chunk_size:

                    if current:
                        current += "\n"

                    current += p

                else:

                    # 保存当前 Chunk
                    if current:
                        results.append(current)

                    # 新 Chunk 从当前段开始
                    current = p

            # 保存最后一个 Chunk
            if current:
                results.append(current)

        return results