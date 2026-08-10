from backend.rag.source_attribution import SourceAttribution

contexts = [
    {
        "document_id": 15,
        "chunk_id": 21,
        "chunk_index": 0,
    },
    {
        "document_id": 17,
        "chunk_id": 29,
        "chunk_index": 3,
    },
]

sources = SourceAttribution.build(contexts)

print("===== Sources =====")

for item in sources:
    print(item)