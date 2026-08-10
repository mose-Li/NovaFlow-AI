import requests


class OllamaClient:

    def __init__(
        self,
        host="http://localhost:11434",
        model="llama3.2",
    ):
        self.host = host
        self.model = model

    def chat(self, prompt: str):

        response = requests.post(
            f"{self.host}/api/generate",
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False,
            },
            timeout=300,
        )

        response.raise_for_status()

        return response.json()["response"]