class ChunkService:
    """
    文本切分服务
    """

    def __init__(
        self,
        max_length=500,
        overlap=50,
    ):
        self.max_length = max_length
        self.overlap = overlap

    def split(self, text: str):

        text = text.strip()

        if not text:
            return []

        # 第一层：按空行切分
        paragraphs = [
            p.strip()
            for p in text.split("\n\n")
            if p.strip()
        ]

        chunks = []

        for paragraph in paragraphs:

            if len(paragraph) <= self.max_length:
                chunks.append(paragraph)

            else:

                start = 0

                while start < len(paragraph):

                    end = start + self.max_length

                    chunks.append(
                        paragraph[start:end]
                    )

                    start = end - self.overlap

        return chunks