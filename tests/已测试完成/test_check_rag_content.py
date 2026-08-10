from backend.repositories.document_repository import DocumentRepository

repo = DocumentRepository()

content = repo.get_document_content(11)

print(content)