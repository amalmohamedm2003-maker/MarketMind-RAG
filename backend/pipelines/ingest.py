import pandas as pd
import os
from datetime import datetime

RAW_PATH = "data/raw"
PROCESSED_PATH = "data/processed"

os.makedirs(PROCESSED_PATH, exist_ok=True)

def load_google_analytics():
    df = pd.read_csv(f"{RAW_PATH}/google_analytics.csv")
    records = []

    for _, row in df.iterrows():
        records.append({
            "source": "google_analytics",
            "channel": row["channel"],
            "metric": "sessions",
            "value": row["sessions"],
            "date": row["date"],
            "business_context": "Traffic acquisition"
        })
        records.append({
            "source": "google_analytics",
            "channel": row["channel"],
            "metric": "conversions",
            "value": row["conversions"],
            "date": row["date"],
            "business_context": "Funnel performance"
        })
    return pd.DataFrame(records)

def load_google_ads():
    df = pd.read_csv(f"{RAW_PATH}/google_ads.csv")
    records = []

    for _, row in df.iterrows():
        records.append({
            "source": "google_ads",
            "channel": row["campaign"],
            "metric": "cost",
            "value": row["cost"],
            "date": str(datetime.now().date()),
            "business_context": "Paid acquisition cost"
        })
        records.append({
            "source": "google_ads",
            "channel": row["campaign"],
            "metric": "conversions",
            "value": row["conversions"],
            "date": str(datetime.now().date()),
            "business_context": "Paid conversion efficiency"
        })
    return pd.DataFrame(records)

def load_seo_keywords():
    df = pd.read_csv(f"{RAW_PATH}/seo_keywords.csv")
    records = []

    for _, row in df.iterrows():
        records.append({
            "source": "seo",
            "channel": "organic",
            "metric": f"keyword:{row['keyword']}",
            "value": row["search_volume"],
            "date": str(datetime.now().date()),
            "business_context": "SEO opportunity analysis"
        })
    return pd.DataFrame(records)

def load_case_studies():
    with open(f"{RAW_PATH}/marketing_cases.txt", "r") as f:
        text = f.read()

    return pd.DataFrame([{
        "source": "case_study",
        "channel": "strategy",
        "metric": "case_text",
        "value": 0,
        "date": str(datetime.now().date()),
        "business_context": text
    }])

def run_pipeline():
    dfs = [
        load_google_analytics(),
        load_google_ads(),
        load_seo_keywords(),
        load_case_studies()
    ]

    final_df = pd.concat(dfs, ignore_index=True)
    final_df.to_csv(f"{PROCESSED_PATH}/marketing_master.csv", index=False)

    print("✅ Day-1 ingestion pipelines completed")
    print(f"Total records: {len(final_df)}")

if __name__ == "__main__":
    run_pipeline()
