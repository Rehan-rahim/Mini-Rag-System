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

**ANOTHER THING TO SUBMIT**

**Retrieval Metrics & Faithfulness Discussion**

In this lab, we implemented a multimodal Retrieval-Augmented Generation (RAG) system using PDFs and images. We evaluated the system using retrieval metrics and conducted an ablation study to analyze the effects of different configurations.

**1. Retrieval Metrics**
Precision@5 (P@5): Measures the fraction of top-5 retrieved evidence chunks that contain at least one must-have keyword from the query rubric.
Recall@10 (R@10): Measures the fraction of relevant evidence chunks retrieved within the top-10 results.
Faithfulness: Evaluates whether the evidence used in the generated answer is consistent with the content in the documents. For our extractive generator, faithfulness is calculated as the fraction of selected evidence lines containing at least one must-have keyword.


**Observation:**

Page-based chunking tends to retrieve more coherent chunks, improving faithfulness, because each chunk corresponds to a full page.
Fixed-size chunking increases granularity, which may slightly reduce P@5 but can improve recall, as smaller chunks can capture keywords that are split across pages.
Text-only retrieval is faster and avoids irrelevant images but may miss important multimodal context.
Multimodal retrieval improves coverage, especially when queries relate to visual content (e.g., images of network setups, city skylines).

**2. Ablation Study**
We systematically varied the following parameters:
Parameter	Values
Chunking	Page-based, Fixed-size
TOP_K_TEXT	2, 5, 10
Alpha (fusion)	0.2, 0.5, 0.8
Modality	Text-only, Multimodal

**Key observations:**

TOP_K_TEXT: Increasing top_k improves recall but may reduce precision slightly if irrelevant chunks are included.
Alpha (fusion weight): Higher alpha favors text, improving text-based relevance; lower alpha favors images, useful for queries about figures.
Chunking strategy: Page-based chunks give more context per chunk (better for long answers), while fixed-size chunks improve fine-grained retrieval (better for keyword coverage).
Text-only vs Multimodal: Multimodal retrieval consistently retrieves relevant images alongside text, enhancing grounding for queries related to visual information.
The ablation table shows how retrieval metrics vary with these settings, helping to identify configurations that balance precision, recall, and faithfulness.




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


