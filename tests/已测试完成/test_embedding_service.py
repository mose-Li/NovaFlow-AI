from backend.embedding.embedding_service import EmbeddingService

service = EmbeddingService()

vector = service.encode("NovaFlow AI")

print("Dimension:", len(vector))
print(vector[:10])