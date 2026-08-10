from uuid import uuid4

from backend.repositories.document_repository import DocumentRepository

repo = DocumentRepository()

repo.create_document(
    original_filename="test.pdf",
    stored_filename=f"{uuid4()}.pdf",
    file_type="pdf",
    mime_type="application/pdf",
    file_size=1024,
    checksum=str(uuid4()),
)

print("Repository Test Passed!")