from backend.rag.vector_search import VectorSearch

vs = VectorSearch()

results = vs.search(
    query="Hello GPT",
    top_k=10,
    threshold=0.35,
)

print("===== Threshold Test =====")

for item in results:
    print(item)