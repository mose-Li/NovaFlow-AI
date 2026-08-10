from backend.rag.rag_service import RAGService

service = RAGService()

result = service.search(
    question="Hello GPT",
    top_k=3,
)

print(result)