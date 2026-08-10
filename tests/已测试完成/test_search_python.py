from backend.rag.rag_service import RAGService

rag = RAGService()

result = rag.search(
    question="Python 有什么特点？",
    top_k=3,
)

print(result)