from backend.services.document_service import DocumentService
from datetime import datetime

service = DocumentService()

content = f"""
Hello NovaFlow AI
Time: {datetime.now()}
""".encode("utf-8")

result = service.upload_document(
    original_filename="hello.txt",
    mime_type="text/plain",
    file_bytes=content,
)

print(result)