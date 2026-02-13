# evaluation/metrics.py
def eval_hits(ctx, qobj, page_chunks):
    must_keywords = qobj.get("rubric", {}).get("must_have_keywords", [])

    # Precision@5
    relevant_count_5 = 0
    for idx, _ in ctx.get("text_hits", [])[:5]:
        chunk_text = page_chunks[idx].text.lower()
        if any(k.lower() in chunk_text for k in must_keywords):
            relevant_count_5 += 1
    P5 = relevant_count_5 / 5 if 5 > 0 else 0.0

    # Recall@10
    relevant_count_10 = 0
    for idx, _ in ctx.get("text_hits", [])[:10]:
        chunk_text = page_chunks[idx].text.lower()
        if any(k.lower() in chunk_text for k in must_keywords):
            relevant_count_10 += 1
    R10 = relevant_count_10 / max(len(must_keywords), 1)

    faith = 1.0  # extractive grounded
    return round(P5, 3), round(R10, 3), faith