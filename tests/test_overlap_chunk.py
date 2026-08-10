from backend.chunk.chunk_engine import ChunkEngine

text = """

第一段

第二段

第三段

第四段

第五段

第六段

第七段

第八段

第九段

第十段

"""

# 为了测试，把 Chunk 调小
ChunkEngine.CHUNK_SIZE = 80

chunks = ChunkEngine.split(text)

print("Chunk Count:", len(chunks))

for chunk in chunks:

    print("=" * 50)
    print(chunk["chunk_index"])
    print(chunk["content"])