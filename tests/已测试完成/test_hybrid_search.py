from backend.retrieval.hybrid_search import HybridSearch

search = HybridSearch()

results = search.search(
    query="RAG 的流程",
    top_k=5,
)

print("===== Hybrid Search =====")

for item in results:

    print(item)