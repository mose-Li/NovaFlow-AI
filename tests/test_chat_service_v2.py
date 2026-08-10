from backend.services.chat_service import ChatService

service = ChatService()

result = service.chat(
    question="RAG 的流程是什么？",
    top_k=3,
)

print("\n========== Question ==========")
print(result["question"])

print("\n========== Answer ==========")
print(result["answer"])

print("\n========== Context ==========")

for item in result["contexts"]:

    print("-" * 60)

    print("Chunk ID :", item["chunk_id"])

    print("Score    :", round(item["rerank_score"], 4))

    print(item["content"])