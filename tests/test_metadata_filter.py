from backend.retrieval.metadata_filter import MetadataFilter

results = [
    {
        "content": "AI",
        "department": "Engineering",
    },
    {
        "content": "HR Policy",
        "department": "HR",
    },
]

filtered = MetadataFilter.filter(
    results,
    {
        "department": "HR",
    },
)

print(filtered)