from backend.retrieval.dynamic_topk import DynamicTopK

results = [
    {"content": "A", "hybrid_score": 0.97},
    {"content": "B", "hybrid_score": 0.91},
    {"content": "C", "hybrid_score": 0.73},
    {"content": "D", "hybrid_score": 0.60},
    {"content": "E", "hybrid_score": 0.42},
    {"content": "F", "hybrid_score": 0.31},
]

selected = DynamicTopK.select(
    results=results,
    min_score=0.55,
    max_top_k=5,
)

print("===== Dynamic Top-K =====")

for item in selected:
    print(item)