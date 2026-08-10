from backend.embedding.embedding_service import EmbeddingService

service = EmbeddingService()

text = """
Hello NovaFlow AI

This is my first embedding test.
"""

vector = service.encode(text)

print("====== Embedding Test ======")
print("Vector Dimension :", len(vector))
print("First 10 Values :")

for value in vector[:10]:
    print(value)