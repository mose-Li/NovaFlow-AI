from backend.rag.rag_service import RAGService

rag = RAGService()

result = rag.search(
    question="RAG 的流程是什么？",
    top_k=3,
)

print(result)