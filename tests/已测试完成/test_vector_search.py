from backend.retrieval.vector_search import VectorSearch

search = VectorSearch()

results = search.search(
    question="Hello NovaFlow AI",
    top_k=5,
)

print("检索结果：")

for item in results:
    print(item)