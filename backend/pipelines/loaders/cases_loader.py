from pathlib import Path

CASES_PATH = Path("backend/data/raw/cases/marketing_cases.txt")

def load_cases():
    records = []
    if not CASES_PATH.exists():
        return records

    with open(CASES_PATH, encoding="utf-8") as f:
        for line in f:
            if line.strip():
                records.append({
                    "text": line.strip(),
                    "source": "case"
                })

    print(f"✅ Cases loaded: {len(records)}")
    return records
