# Mini-Rag-System
Mini RAG System: Transformers, Embeddings &amp; Vector Retrieval (Git-> Colab-> Hugging Face-> FAISS

SECTION: LAB 02

Results table:
P@5_keyword	R@10_keyword	P@5_vector	R@10_vector	P@5_hybrid	R@10_hybrid	query	alpha_used	num_relevant_labeled
0	0.0	0.0	0.0	0.0	0.0	0.0	Q1: What are the key benefits of implementing ...	0.8	0
1	0.0	0.0	0.0	0.0	0.0	0.0	Q2: How can hospitals optimize patient flow us...	0.2	0
2	0.0	0.0	0.0	0.0	0.0	0.0	Q3 (ambiguous): Can AI in healthcare completel...	0.2	0

Screenshots: chunking comparison, reranking before/after, prompt-only vs RAG answers


Reflection (3–5 sentences): one failure case, which layer failed, one concrete fix:
ANS: One failure case occurred when the retrieval missed key chunks for Q3 (ambiguous query), resulting in the generator producing incomplete answers. The retrieval layer failed due to low keyword overlap and semantic confusion. A concrete fix is to tune α in hybrid search or increase the candidate pool size to improve recall.
