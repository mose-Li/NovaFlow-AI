from backend.repositories.document_repository import DocumentRepository

repo = DocumentRepository()

docs = repo.list_documents()

print("Document Count:", len(docs))

for doc in docs:
    print(doc)