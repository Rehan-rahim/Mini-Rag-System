"""
FastAPI Backend - SIMPLIFIED
"""

from fastapi import FastAPI
from pydantic import BaseModel
from rag.Lab3_core import load_dataset
from rag.pipeline import RAGPipeline

app = FastAPI(title="RAG Backend API")

# Load data once at startup
print("Loading dataset...")
load_dataset()

# Initialize RAG Pipeline
rag = RAGPipeline()


class QueryRequest(BaseModel):
    question: str
    top_k_text: int = 5
    top_k_images: int = 3
    alpha: float = 0.5


@app.get("/")
def root():
    return {"status": "ok", "message": "RAG API is running"}


@app.post("/query")
def query_rag(req: QueryRequest):
    """
    Query the RAG system
    """
    qobj = {
        "question": req.question,
        "rubric": {"must_have_keywords": []}
    }
    
    result = rag.query(
        qobj,
        top_k_text=req.top_k_text,
        top_k_images=req.top_k_images,
        alpha=req.alpha
    )
    
    return result