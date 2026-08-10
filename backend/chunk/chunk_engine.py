from backend.chunk.smart_merge import SmartMerge
from backend.chunk.semantic_chunk import SemanticChunk


class ChunkEngine:
    """
    企业级 Chunk Engine v2
    """

    # 单个 Chunk 最大长度
    CHUNK_SIZE = 500

    # 相邻 Chunk 保留几个 Section
    OVERLAP_PARAGRAPHS = 1

    @classmethod
    def split(cls, text: str):

        # ==========================
        # 1. 清理空段
        # ==========================
        paragraphs = []

        for p in text.split("\n"):
            p = p.strip()

            if p:
                paragraphs.append(p)

        if not paragraphs:
            return []

        # ==========================
        # 2. Smart Merge
        # ==========================
        paragraphs = SmartMerge.merge(paragraphs)

        # ==========================
        # 3. Semantic Section
        # ==========================
        sections = SemanticChunk.build_sections(paragraphs)

        # ==========================
        # 4. 超长 Section 自动切分
        # ==========================
        sections = SemanticChunk.split_large_sections(
            sections,
            chunk_size=cls.CHUNK_SIZE,
        )

        # ==========================
        # 5. Build Chunks
        # ==========================
        chunks = []

        current_chunk = []
        current_length = 0
        chunk_index = 0

        i = 0

        while i < len(sections):

            section = sections[i]

            # 当前 Chunk 可以放下
            if current_length + len(section) <= cls.CHUNK_SIZE:

                current_chunk.append(section)

                current_length += len(section) + 1

                i += 1

                continue

            # --------------------------
            # Chunk 已有内容
            # 保存当前 Chunk
            # --------------------------
            if current_chunk:

                content = "\n".join(current_chunk)

                chunks.append(
                    {
                        "chunk_index": chunk_index,
                        "content": content,
                        "token_count": len(content),
                    }
                )

                chunk_index += 1

                # Overlap
                overlap = current_chunk[-cls.OVERLAP_PARAGRAPHS:]

                current_chunk = overlap.copy()

                current_length = sum(
                    len(x) + 1
                    for x in current_chunk
                )

                continue

            # --------------------------
            # 当前 Chunk 为空
            # section 自己超过 ChunkSize
            # 防止死循环
            # --------------------------
            chunks.append(
                {
                    "chunk_index": chunk_index,
                    "content": section,
                    "token_count": len(section),
                }
            )

            chunk_index += 1

            i += 1

        # ==========================
        # 保存最后一个 Chunk
        # ==========================
        if current_chunk:

            content = "\n".join(current_chunk)

            chunks.append(
                {
                    "chunk_index": chunk_index,
                    "content": content,
                    "token_count": len(content),
                }
            )

        return chunks