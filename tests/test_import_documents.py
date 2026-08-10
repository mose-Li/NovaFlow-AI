from pathlib import Path

from backend.services.document_service import DocumentService

service = DocumentService()

folder = Path("tests/data")

for file in folder.glob("*.txt"):

    with open(file, "rb") as f:

        result = service.upload_document(
            original_filename=file.name,
            mime_type="text/plain",
            file_bytes=f.read(),
        )

        print(result)