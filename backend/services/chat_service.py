from backend.llm.llm_service import LLMService

from backend.rag.prompt_builder import PromptBuilder
from backend.rag.context_cleaner import ContextCleaner
from backend.rag.context_deduplicator import ContextDeduplicator
from backend.rag.source_attribution import SourceAttribution

from backend.retrieval.hybrid_search import HybridSearch
from backend.retrieval.reranker import Reranker


class ChatService:
    """
    Enterprise RAG Chat Service

    Pipeline

        User Question
              ↓
        Hybrid Search
              ↓
        Reranker
              ↓
        Context Cleaner
              ↓
        Context Deduplicator
              ↓
        Source Attribution
              ↓
        Prompt Builder
              ↓
        LLM
              ↓
        Response
    """

    def __init__(self):

        self.hybrid_search = HybridSearch()
        self.reranker = Reranker()
        self.prompt_builder = PromptBuilder()
        self.llm = LLMService()

    # ==================================================
    # Chat
    # ==================================================

    def chat(
        self,
        question: str,
        top_k: int = 5,
    ):

        # ------------------------------------------
        # Hybrid Retrieval
        # ------------------------------------------

        candidates = self.hybrid_search.search(
            query=question,
        )

        # ------------------------------------------
        # Reranker
        # ------------------------------------------

        contexts = self.reranker.rerank(
            query=question,
            candidates=candidates,
            top_k=top_k,
        )

        # ------------------------------------------
        # Context Cleaner
        # ------------------------------------------

        contexts = ContextCleaner.clean_contexts(
            contexts
        )

        # ------------------------------------------
        # Context Deduplicator
        # ------------------------------------------

        contexts = ContextDeduplicator.deduplicate(
            contexts
        )

        # ------------------------------------------
        # Source Attribution
        # ------------------------------------------

        sources = SourceAttribution.build(
            contexts
        )

        # ------------------------------------------
        # Prompt Builder
        # ------------------------------------------

        prompt = self.prompt_builder.build(
            question=question,
            contexts=contexts,
        )

        # ------------------------------------------
        # LLM Generation
        # ------------------------------------------

        answer = self.llm.chat(
            prompt
        )

        # ------------------------------------------
        # Response
        # ------------------------------------------

        return {
            "question": question,
            "answer": answer,
            "contexts": contexts,
            "sources": sources,
        }