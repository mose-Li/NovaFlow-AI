from dataclasses import dataclass, field


@dataclass
class RetrievalRequest:
    """
    Enterprise Retrieval Request
    """

    query: str

    top_k: int = 5

    vector_top_k: int = 10

    bm25_top_k: int = 10

    metadata: dict = field(default_factory=dict)