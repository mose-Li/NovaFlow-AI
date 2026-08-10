from backend.repositories.document_repository import DocumentRepository

repo = DocumentRepository()

result = repo.get_by_checksum("abcdefg")

print(result)