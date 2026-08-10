from fastapi import APIRouter
from pydantic import BaseModel

from backend.rag.rag_service import RAGService

router = APIRouter(
    prefix="/rag",
    tags=["RAG"],
)

service = RAGService()


class SearchRequest(BaseModel):
    question: str
    top_k: int = 5


@router.post("/search")
async def rag_search(request: SearchRequest):

    result = service.search(
        question=request.question,
        top_k=request.top_k,
    )

    return result