from backend.chunk.smart_merge import SmartMerge

paragraphs = [
    "Python",
    "特点：",
    "简单",
    "易学习",
    "跨平台",
    "生态丰富",
]

result = SmartMerge.merge(paragraphs)

print("===== Merge Result =====")

for item in result:
    print("-" * 40)
    print(item)