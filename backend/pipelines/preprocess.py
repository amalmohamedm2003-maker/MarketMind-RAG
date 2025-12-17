import pandas as pd

INPUT_PATH = "data/processed/marketing_master.csv"
OUTPUT_PATH = "data/processed/marketing_clean.csv"

def preprocess():
    df = pd.read_csv(INPUT_PATH)

    df.fillna("", inplace=True)

    df["semantic_text"] = df.apply(
        lambda x: f"""
        Source: {x['source']}
        Channel/Campaign: {x['channel']}
        Metric: {x['metric']}
        Value: {x['value']}
        Business Context: {x['business_context']}
        Date: {x['date']}
        """.strip(),
        axis=1
    )

    df.to_csv(OUTPUT_PATH, index=False)
    print("✅ Preprocessing completed")

if __name__ == "__main__":
    preprocess()
