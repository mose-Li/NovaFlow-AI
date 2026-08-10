from backend.llm.ollama_client import OllamaClient

client = OllamaClient()

answer = client.chat("你好，请介绍一下你自己。")

print(answer)