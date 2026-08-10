from backend.chunk.semantic_chunk import SemanticChunk

paragraphs = [

    "Python",

    "特点：",

    "简单",

    "易学习",

    "跨平台",

    "应用：",

    "AI开发",

    "Web开发",

    "自动化",

]

sections = SemanticChunk.build_sections(paragraphs)

print("===== Sections =====")

for i, s in enumerate(sections):

    print("=" * 40)

    print(i)

    print(s)