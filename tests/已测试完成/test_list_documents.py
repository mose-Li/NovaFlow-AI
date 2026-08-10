from backend.repositories.document_repository import DocumentRepository

repo = DocumentRepository()

rows = repo.list_documents()

print(f"Total Documents: {len(rows)}")

for row in rows:
    print(row)