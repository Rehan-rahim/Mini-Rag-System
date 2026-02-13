"""
Streamlit App - SIMPLIFIED NO BACKEND VERSION
Works standalone without FastAPI
"""

import os
import csv
from datetime import datetime
import streamlit as st

# Add parent to path
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#from rag.Lab3_core import load_dataset, build_context, page_chunks
from evaluation.metrics import eval_hits
import time

st.set_page_config(page_title="AI Big Data Copilot", layout="wide")
st.title("📊 Lab 4 - RAG Application")

# Initialize data
if 'initialized' not in st.session_state:
    with st.spinner("Loading data..."):
        load_dataset()
        st.session_state.initialized = True
        st.success("✅ Data loaded!")


# CSV Logger
def log_query(row):
    os.makedirs("logs", exist_ok=True)
    path = "logs/query_metrics.csv"
    write_header = not os.path.exists(path)
    with open(path, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(["timestamp", "query", "latency", "P@5", "R@10", "faithfulness"])
        writer.writerow(row)


# Sidebar
st.sidebar.header("Settings")
top_k_text = st.sidebar.slider("Top-K Text", 1, 10, 5)
top_k_images = st.sidebar.slider("Top-K Images", 0, 5, 3)
alpha = st.sidebar.slider("Alpha (text vs images)", 0.0, 1.0, 0.5)

# Main query interface
query = st.text_area("Enter your question:", height=100)

if st.button("🔍 Search", type="primary") and query:
    qobj = {
        "question": query,
        "rubric": {"must_have_keywords": ["retrieval", "rag", "evidence"]}
    }
    
    start = time.time()
    
    with st.spinner("Searching..."):
        ctx = build_context(
            query,
            top_k_text=top_k_text,
            top_k_images=top_k_images,
            alpha=alpha
        )
    
    P5, R10, faith = eval_hits(ctx, qobj, page_chunks)
    latency = round(time.time() - start, 3)
    
    # Display results
    st.success("✅ Search complete!")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Latency", f"{latency}s")
    with col2:
        st.metric("P@5", f"{P5:.2f}")
    with col3:
        st.metric("R@10", f"{R10:.2f}")
    with col4:
        st.metric("Faithful", "✅" if faith > 0.5 else "❌")
    
    st.subheader("📝 Answer")
    st.info(ctx.get("answer", "No answer generated"))
    
    st.subheader("📄 Retrieved Evidence")
    for i, line in enumerate(ctx.get("context", [])[:5], 1):
        st.write(f"{i}. {line}")
    
    if ctx.get("image_paths"):
        st.subheader("🖼️ Retrieved Images")
        for img_path in ctx["image_paths"]:
            if os.path.exists(img_path):
                st.image(img_path, width=400)
    
    # Log
    log_query([datetime.now().isoformat(), query, latency, P5, R10, faith])
    st.caption("✅ Query logged to logs/query_metrics.csv")

# Footer
st.markdown("---")
st.caption("CS 5542 Lab 4 - Rehan Ali")
