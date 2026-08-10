from backend.chunk.chunk_engine import ChunkEngine

text = "Hello GPT! " * 200

chunks = ChunkEngine.split(text)

print("Chunk 数量：", len(chunks))

for chunk in chunks:
    print(chunk)