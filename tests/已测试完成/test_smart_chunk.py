from backend.chunk.chunk_engine import ChunkEngine

text = """
NovaFlow AI 是企业AI平台。

主要功能包括：

文档管理

RAG知识库

AI聊天

工作流自动化

智能Agent

Python开发

企业知识库
"""

chunks = ChunkEngine.split(text)

print("Chunk Count:", len(chunks))

for chunk in chunks:

    print("=" * 50)

    print(chunk["chunk_index"])

    print(chunk["content"])