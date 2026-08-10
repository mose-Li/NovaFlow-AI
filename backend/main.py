from fastapi import FastAPI

from backend.api.documents import router as document_router
from backend.api.rag import router as rag_router
from backend.core.logger import app_logger

app = FastAPI(
    title="NovaFlow AI",
    version="0.3.0",
    description="AI Business Automation Platform",
)

# Documents API
app.include_router(document_router)

# RAG API
app.include_router(rag_router)


@app.get("/")
async def root():
    return {
        "message": "Welcome to NovaFlow AI"
    }


@app.get("/health")
async def health_check():

    app_logger.info("Health check called")

    return {
        "status": "ok",
        "version": "0.3.0"
    }