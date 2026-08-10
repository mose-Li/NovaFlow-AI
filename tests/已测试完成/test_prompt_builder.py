from backend.rag.prompt_builder import PromptBuilder

contexts = [
    {
        "content": "NovaFlow AI 是一个 AI 自动化平台。"
    },
    {
        "content": "它支持 RAG 检索。"
    }
]

prompt = PromptBuilder.build(
    question="NovaFlow AI 是什么？",
    contexts=contexts,
)

print(prompt)