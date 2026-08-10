from backend.llm.ollama_client import OllamaClient


class LLMService:

    def __init__(self):
        self.client = OllamaClient(
            model="llama3.2"
        )

    def chat(self, prompt: str):
        return self.client.chat(prompt)