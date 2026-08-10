from backend.chunk.semantic_chunk import SemanticChunk

long_text = "特点：\n"

for i in range(80):
    long_text += f"这是第{i}段内容。\n"

sections = [long_text]

chunks = SemanticChunk.split_large_sections(
    sections,
    chunk_size=120,
)

print("Chunk Count:", len(chunks))

for i, chunk in enumerate(chunks):

    print("=" * 50)
    print(i)
    print("Length:", len(chunk))
    print(chunk)