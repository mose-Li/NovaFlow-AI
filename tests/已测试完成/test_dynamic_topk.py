from backend.rag.vector_search import VectorSearch

vs = VectorSearch()

results = vs.search(
    query="Hello GPT",
    top_k=5,
    threshold=0.35,
)

print("Result Count:", len(results))

for item in results:
    print(item)