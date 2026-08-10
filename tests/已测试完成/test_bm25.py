from backend.retrieval.bm25_search import BM25Search

bm25 = BM25Search()

results = bm25.search(
    query="RAG 的流程",
    top_k=5,
)

print("===== BM25 Search =====")

for item in results:
    print(item)