from backend.retrieval.diversity_filter import DiversityFilter

results = [
    {"document_id": 1, "content": "A1"},
    {"document_id": 1, "content": "A2"},
    {"document_id": 1, "content": "A3"},
    {"document_id": 2, "content": "B1"},
    {"document_id": 2, "content": "B2"},
    {"document_id": 3, "content": "C1"},
]

filtered = DiversityFilter.diversify(
    results,
    max_chunks_per_document=2,
)

for item in filtered:
    print(item)