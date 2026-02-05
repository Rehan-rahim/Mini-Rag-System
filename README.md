LAB 03 SECTION AND DELIVERABLES (I have uploaded both tables/grids here, and as per the Lab instructor, no need for Screenshots if the grid is uploaded to the README file

**BEFORE ABLATION**

id	P@5	R@10	total_relevant_chunks
0	Q1	0.50	1.0	2
1	Q2	0.25	1.0	1
2	Q3	0.25	1.0	1
3	Q4	0.25	1.0	1
4	Q5	0.25	1.0	1
5	Q6	0.00	0.0	0

**AFTER ABLATION STUDY**

query_id	chunk_type	modality	top_k_text	alpha	P@5	R@10	faithfulness
0	Q1	page	text_only	2	0.2	1.0	0.2	1.0
1	Q1	page	multimodal	2	0.2	0.4	0.2	0.4
2	Q1	page	text_only	2	0.5	1.0	0.2	1.0
3	Q1	page	multimodal	2	0.5	0.4	0.2	0.4
4	Q1	page	text_only	2	0.8	1.0	0.2	1.0
...	...	...	...	...	...	...	...	...
211	Q6	fixed	multimodal	10	0.2	0.0	0.0	0.0
212	Q6	fixed	text_only	10	0.5	0.0	0.0	0.0
213	Q6	fixed	multimodal	10	0.5	0.0	0.0	0.0
214	Q6	fixed	text_only	10	0.8	0.0	0.0	0.0
215	Q6	fixed	multimodal	10	0.8	0.0	0.0	0.0
216 rows × 8 columns




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


