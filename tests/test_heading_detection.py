from backend.chunk.semantic_chunk import SemanticChunk

tests = [

    "特点：",

    "应用：",

    "Python",

    "1. 安装",

    "2) 配置",

    "（一）简介",

    "# 标题",

    "这是正文",

]

for t in tests:

    print(t, "=>", SemanticChunk.is_heading(t))