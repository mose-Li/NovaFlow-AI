from backend.retrieval.hybrid_search import HybridSearch
from backend.retrieval.reranker import Reranker

query = "RAG 的流程是什么？"

hybrid = HybridSearch()

candidates = hybrid.search(
    query=query,
    top_k=10,
)

reranker = Reranker()

results = reranker.rerank(
    query=query,
    candidates=candidates,
    top_k=5,
)

print("===== Rerank Result =====")

for item in results:

    print(
        {
            "chunk_id": item["chunk_id"],
            "rerank_score": round(
                item["rerank_score"],
                4,
            ),
            "content": item["content"],
        }
    )