"""
Enterprise BM25 Sparse Retrieval

Provides sparse retrieval using the BM25 ranking algorithm.

Version:
    v0.5.0
"""

from rank_bm25 import BM25Okapi

from backend.repositories.document_repository import DocumentRepository


class BM25Search:
    """
    Enterprise BM25 Retriever.
    """

    def __init__(self):

        self.repository = DocumentRepository()

        self.documents = []

        self.corpus = []

        self.bm25 = None

        self._build_index()

    # ==================================================
    # Step 1: Build BM25 Index
    # ==================================================
    def _build_index(self) -> None:

        self.documents = self.repository.list_all_chunks()

        self.corpus = []

        for chunk in self.documents:

            content = chunk[3]

            tokens = self.tokenize(content)

            self.corpus.append(tokens)

        self.bm25 = BM25Okapi(self.corpus)

    # ==================================================
    # Step 2: Tokenize Text
    # ==================================================
    @staticmethod
    def tokenize(text: str) -> list[str]:

        if not text:
            return []

        text = (
            text.replace("\n", " ")
                .replace("：", " ")
                .replace("，", " ")
                .replace("。", " ")
                .replace("（", " ")
                .replace("）", " ")
                .replace("(", " ")
                .replace(")", " ")
                .replace(",", " ")
                .replace(".", " ")
        )

        return text.split()

    # ==================================================
    # Step 3: BM25 Search
    # ==================================================
    def search(
        self,
        query: str,
        top_k: int = 5,
    ) -> list[dict]:

        # Empty query
        if not query.strip():
            return []

        # Empty index
        if not self.documents or self.bm25 is None:
            return []

        query_tokens = self.tokenize(query)

        if not query_tokens:
            return []

        scores = self.bm25.get_scores(query_tokens)

        results = []

        for index, score in enumerate(scores):

            if score <= 0:
                continue

            chunk = self.documents[index]

            results.append(
                {
                    "chunk_id": chunk[0],
                    "document_id": chunk[1],
                    "chunk_index": chunk[2],
                    "content": chunk[3],
                    "score": float(score),
                }
            )

        results.sort(
            key=lambda x: x["score"],
            reverse=True,
        )

        return results[:top_k]