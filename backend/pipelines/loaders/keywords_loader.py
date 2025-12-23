from pathlib import Path

KEYWORDS_PATH = Path("backend/data/raw/keywords/keywords.txt")

def load_keywords():
    records = []
    if not KEYWORDS_PATH.exists():
        return records

    with open(KEYWORDS_PATH, encoding="utf-8") as f:
        for line in f:
            kw = line.strip()
            if kw:
                records.append({
                    "text": f"Important marketing keyword: {kw}",
                    "source": "keywords"
                })

    print(f"✅ Keywords loaded: {len(records)}")
    return records
