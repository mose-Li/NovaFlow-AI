import json

from sentence_transformers import SentenceTransformer


class EmbeddingService:

    def __init__(self):

        self.model_name = "all-MiniLM-L6-v2"

        self.model = SentenceTransformer(
            self.model_name
        )

    def encode(self, text: str):

        vector = self.model.encode(
            text,
            normalize_embeddings=True,
        )

        return vector.tolist()

    def encode_json(self, text: str):

        vector = self.encode(text)

        return json.dumps(vector)