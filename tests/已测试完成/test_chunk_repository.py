from backend.repositories.document_repository import DocumentRepository

repo = DocumentRepository()

repo.save_chunk(
    document_id=1,
    chunk_index=0,
    content="Hello GPT",
    token_count=2,
)

rows = repo.list_chunks(1)

for row in rows:
    print(row)