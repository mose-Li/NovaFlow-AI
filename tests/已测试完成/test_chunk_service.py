from backend.chunk.chunk_service import ChunkService

text = """
NovaFlow AI 是一个企业 AI 自动化平台。

它支持文档管理。

支持 RAG。

支持 AI Chat。

支持 Workflow。
"""

service = ChunkService()

chunks = service.split(text)

for i, chunk in enumerate(chunks):

    print("=" * 40)
    print(i)
    print(chunk)