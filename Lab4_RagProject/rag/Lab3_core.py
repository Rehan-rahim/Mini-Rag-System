"""
Lab 3 Core - SIMPLIFIED VERSION
All in one file - no complex imports
"""

import os
import glob
import re
from dataclasses import dataclass
from typing import List, Dict, Any
import numpy as np
#from sklearn.feature_extraction.text import TfidfVectorizer
#from sklearn.preprocessing import normalize


# ===== DATA CLASSES =====
@dataclass
class TextChunk:
    chunk_id: str
    doc_id: str
    page_num: int
    text: str


@dataclass
class ImageItem:
    item_id: str
    path: str
    caption: str


# ===== GLOBALS (loaded once) =====
page_chunks: List[TextChunk] = []
image_items: List[ImageItem] = []
text_vec = None
text_X = None
img_vec = None
img_X = None


# ===== HELPER FUNCTIONS =====
def clean_text(s: str) -> str:
    s = s or ""
    s = re.sub(r"\s+", " ", s).strip()
    return s


def load_dataset():
    """Load data from project_data_mm folder"""
    global page_chunks, image_items, text_vec, text_X, img_vec, img_X
    
    DATA_DIR = "project_data_mm"
    FIG_DIR = os.path.join(DATA_DIR, "Images")
    
    # Load text files
    txt_files = glob.glob(os.path.join(DATA_DIR, "*.txt"))
    page_chunks = []
    for filepath in txt_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            text = clean_text(f.read())
        if text:
            doc_id = os.path.basename(filepath)
            page_chunks.append(TextChunk(
                chunk_id=f"{doc_id}::p1",
                doc_id=doc_id,
                page_num=1,
                text=text
            ))
    
    # Load images
    image_items = []
    if os.path.exists(FIG_DIR):
        img_files = glob.glob(os.path.join(FIG_DIR, "*.*"))
        for filepath in img_files:
            if filepath.lower().endswith(('.png', '.jpg', '.jpeg')):
                filename = os.path.basename(filepath)
                caption = os.path.splitext(filename)[0].replace("_", " ")
                image_items.append(ImageItem(
                    item_id=filename,
                    path=filepath,
                    caption=caption
                ))
    
    # Build indexes
    if page_chunks:
        corpus = [c.text for c in page_chunks]
        text_vec = TfidfVectorizer(lowercase=True, stop_words="english")
        text_X = text_vec.fit_transform(corpus)
        text_X = normalize(text_X)
    
    if image_items:
        corpus = [it.caption for it in image_items]
        img_vec = TfidfVectorizer(lowercase=True, stop_words="english")
        img_X = img_vec.fit_transform(corpus)
        img_X = normalize(img_X)
    
    print(f"✅ Loaded {len(page_chunks)} text chunks and {len(image_items)} images")
    
    return {
        "text_chunks": page_chunks,
        "image_items": image_items
    }


def tfidf_retrieve(query: str, vec, X, top_k: int = 5):
    """Retrieve top-k results"""
    if vec is None or X is None:
        return []
    q = vec.transform([query])
    q = normalize(q)
    scores = (X @ q.T).toarray().ravel()
    idx = np.argsort(-scores)[:top_k]
    return [(int(i), float(scores[i])) for i in idx]


def build_context(
    question: str,
    text_chunks=None,
    image_chunks=None,
    top_k_text: int = 5,
    top_k_images: int = 3,
    alpha: float = 0.5
) -> Dict[str, Any]:
    """Build context from retrieval"""
    global page_chunks, image_items
    global text_vec, text_X, img_vec, img_X
    
    # Local aliases
    global_chunks = page_chunks
    global_images = image_items
    
    chunks = text_chunks or global_chunks
    images = image_chunks or global_images
    
    # Retrieve
    text_hits = tfidf_retrieve(question, text_vec, text_X, top_k=top_k_text)
    img_hits = tfidf_retrieve(question, img_vec, img_X, top_k=top_k_images)
    
    # Build evidence
    evidence = []
    context_lines = []
    image_paths = []
    
    for idx, score in text_hits:
        if idx < len(chunks):
            ch = chunks[idx]
            snippet = ch.text[:200]
            evidence.append({
                "modality": "text",
                "id": ch.chunk_id,
                "text": snippet,
                "score": score
            })
            context_lines.append(f"[{ch.chunk_id}] {snippet}...")
    
    for idx, score in img_hits:
        if idx < len(images):
            it = images[idx]
            evidence.append({
                "modality": "image",
                "id": it.item_id,
                "text": it.caption,
                "score": score
            })
            image_paths.append(it.path)
            context_lines.append(f"[IMAGE: {it.item_id}] {it.caption}")
    
    # Generate simple answer
    answer = f"Based on retrieved evidence: {context_lines[0] if context_lines else 'No evidence found'}"
    
    return {
        "question": question,
        "answer": answer,
        "evidence": evidence,
        "context": context_lines,
        "image_paths": image_paths,
        "text_hits": text_hits,
        "img_hits": img_hits
    }
