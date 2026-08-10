from backend.repositories.document_repository import DocumentRepository

repo = DocumentRepository()

result = repo.get_chunk_with_document(1)

print(result)