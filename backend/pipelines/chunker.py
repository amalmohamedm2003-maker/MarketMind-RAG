def chunk_documents(documents, size=400):
    chunks = []
    for d in documents:
        text = d["text"]
        for i in range(0, len(text), size):
            chunks.append({
                "text": text[i:i+size],
                "source": d["source"]
            })
    return chunks
