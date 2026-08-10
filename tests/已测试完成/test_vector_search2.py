from backend.rag.vector_search import VectorSearch

search = VectorSearch()

results = search.search(
    "Hello NovaFlow AI",
    top_k=3,
)

print("====== Search Result ======")

for item in results:
    print(item)