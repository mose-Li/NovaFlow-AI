from backend.embedding.embedding_service import EmbeddingService
from backend.repositories.embedding_repository import EmbeddingRepository

embedding_service = EmbeddingService()
repository = EmbeddingRepository()

vector = embedding_service.encode("Hello NovaFlow AI")

repository.save_embedding(
    chunk_id=1,
    model_name="all-MiniLM-L6-v2",
    embedding=vector,
)

result = repository.get_embedding(1)

print(result)