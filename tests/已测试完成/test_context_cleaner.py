from backend.rag.context_cleaner import ContextCleaner


contexts = [
    {
        "content": """



RAG 的流程包括：


Document

↓

Chunk


Embedding




"""
    }
]

result = ContextCleaner.clean_contexts(contexts)

print("===== Clean Result =====")
print(result[0]["content"])