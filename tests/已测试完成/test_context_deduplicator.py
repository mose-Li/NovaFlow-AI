from backend.rag.context_deduplicator import ContextDeduplicator

contexts = [
    {"content": "NovaFlow AI 是企业 AI 自动化平台。"},
    {"content": "NovaFlow AI 是企业 AI 自动化平台。"},
    {"content": "Python 是高级编程语言。"},
]

result = ContextDeduplicator.deduplicate(contexts)

print("===== Deduplicate Result =====")

for item in result:
    print(item["content"])