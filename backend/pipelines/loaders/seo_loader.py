import csv
from pathlib import Path

SEO_PATH = Path("backend/data/raw/seo/seo.csv")

def load_seo():
    records = []
    if not SEO_PATH.exists():
        return records

    with open(SEO_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            text = (
                f"SEO Page {row['page']} has {row['clicks']} clicks, "
                f"{row['impressions']} impressions, CTR {row['ctr']}, "
                f"average position {row['position']}."
            )
            records.append({"text": text, "source": "seo"})

    print(f"✅ SEO records loaded: {len(records)}")
    return records
