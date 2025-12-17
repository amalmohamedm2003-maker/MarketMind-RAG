import pandas as pd
import json
from tqdm import tqdm

INPUT_PATH = "data/processed/marketing_clean.csv"
OUTPUT_PATH = "data/processed/chunks.json"

MAX_TOKENS = 180  # optimal for MiniLM

def chunk_text(text, max_tokens=MAX_TOKENS):
    words = text.split()
    chunks = []
    current = []

    for word in words:
        current.append(word)
        if len(current) >= max_tokens:
            chunks.append(" ".join(current))
            current = []

    if current:
        chunks.append(" ".join(current))

    return chunks

def generate_chunks():
    df = pd.read_csv(INPUT_PATH)
    all_chunks = []

    for _, row in tqdm(df.iterrows(), total=len(df)):
        chunks = chunk_text(row["semantic_text"])

        for idx, chunk in enumerate(chunks):
            all_chunks.append({
                "chunk_id": f"{row['source']}_{idx}",
                "text": chunk,
                "source": row["source"],
                "channel": row["channel"],
                "metric": row["metric"]
            })

    with open(OUTPUT_PATH, "w") as f:
        json.dump(all_chunks, f, indent=2)

    print(f"✅ Created {len(all_chunks)} intelligent chunks")

if __name__ == "__main__":
    generate_chunks()
