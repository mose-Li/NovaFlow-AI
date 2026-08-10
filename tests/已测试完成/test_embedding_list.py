from backend.repositories.embedding_repository import EmbeddingRepository

repo = EmbeddingRepository()

rows = repo.list_embeddings()

print("Embedding数量：", len(rows))

for row in rows:
    print(row)