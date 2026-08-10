from backend.repositories.document_repository import DocumentRepository

repo = DocumentRepository()

documents = repo.list_documents()

for doc in documents:

    print("=" * 60)
    print(f"Document ID : {doc[0]}")
    print(f"Filename    : {doc[1]}")
    print("=" * 60)

    chunks = repo.list_chunks(doc[0])

    print(f"Chunk Count : {len(chunks)}")
    print()

    for chunk in chunks:

        print(f"Chunk {chunk[2]}")
        print("-" * 40)
        print(chunk[3])
        print()