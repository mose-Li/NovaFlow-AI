from backend.embedding.embedding_service import EmbeddingService
from backend.repositories.embedding_repository import EmbeddingRepository

embedder = EmbeddingService()
repo = EmbeddingRepository()

vector = embedder.encode("NovaFlow AI RAG")

embedding_id = repo.save_embedding(
    chunk_id=1,
    model_name=embedder.model_name,
    embedding=vector,
    dimension=len(vector),
)

print("Embedding ID:", embedding_id)

row = repo.get_embedding(1)

print(row)