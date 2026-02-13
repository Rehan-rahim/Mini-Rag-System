"""
RAG Pipeline - SIMPLIFIED
"""

import time
from rag.Lab3_core import build_context, page_chunks, image_items
from evaluation.metrics import eval_hits


class RAGPipeline:
    def __init__(self):
        self.page_chunks = page_chunks
        self.image_items = image_items
    
    def query(self, qobj, top_k_text=5, top_k_images=3, alpha=0.5):
        """Process a single query"""
        question = qobj["question"]
        
        start = time.time()
        
        ctx = build_context(
            question,
            text_chunks=self.page_chunks,
            image_items=self.image_items,
            top_k_text=top_k_text,
            top_k_images=top_k_images,
            alpha=alpha
        )
        
        P5, R10, faith = eval_hits(ctx, qobj, self.page_chunks)
        latency = round(time.time() - start, 3)
        
        return {
            "answer": ctx.get("answer", "No answer generated."),
            "evidence": ctx.get("evidence", []),
            "context": ctx.get("context", []),
            "image_paths": ctx.get("image_paths", []),
            "latency": latency,
            "P@5": P5,
            "R@10": R10,
            "faithfulness": faith
        }