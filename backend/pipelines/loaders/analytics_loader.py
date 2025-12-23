import csv
from pathlib import Path

ANALYTICS_PATH = Path("backend/data/raw/analytics/google_analytics.csv")

def load_analytics():
    records = []
    if not ANALYTICS_PATH.exists():
        return records

    with open(ANALYTICS_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            text = (
                f"Page {row['pagePath']} has {row['sessions']} sessions, "
                f"bounce rate {row['bounceRate']}, "
                f"average session duration {row['avgSessionDuration']} seconds."
            )
            records.append({"text": text, "source": "analytics"})

    print(f"✅ Analytics records loaded: {len(records)}")
    return records
