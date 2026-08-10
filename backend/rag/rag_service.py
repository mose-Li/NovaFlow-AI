from backend.rag.vector_search import VectorSearch
from backend.rag.prompt_builder import PromptBuilder
from backend.llm.llm_service import LLMService


class RAGService:

    def __init__(self):
        self.vector_search = VectorSearch()
        self.llm = LLMService()

    # ==========================
    # RAG 检索
    # ==========================
    def search(
        self,
        question: str,
        top_k: int = 5,
    ):

        results = self.vector_search.search(
            query=question,
            top_k=top_k,
            threshold=0.30,
        )

        contexts = []

        for item in results:

            contexts.append({
                "chunk_id": item["chunk_id"],
                "document_id": item["document_id"],
                "chunk_index": item["chunk_index"],
                "score": round(item["score"], 4),
                "content": item["content"],
            })

        return {
            "question": question,
            "top_k": top_k,
            "contexts": contexts,
        }

    # ==========================
    # AI 问答
    # ==========================
    def chat(
        self,
        question: str,
        top_k: int = 5,
    ):

        # ① 向量检索
        result = self.search(
            question=question,
            top_k=top_k,
        )

        contexts = result["contexts"]

        # ② 构造 Prompt
        prompt = PromptBuilder.build(
            question=question,
            contexts=contexts,
        )

        # ③ 调用 LLM
        answer = self.llm.chat(prompt)

        # ④ 返回结果
        return {
            "question": question,
            "answer": answer,
            "contexts": contexts,
        }