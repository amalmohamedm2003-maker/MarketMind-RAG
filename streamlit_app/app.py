import streamlit as st
import pandas as pd
import requests

# =========================
# App Config
# =========================
st.set_page_config(
    page_title="MarketMind – Marketing Intelligence",
    layout="wide"
)

API_URL = "http://localhost:8000/analyze"

st.title("📊 MarketMind – SEO & Analytics Intelligence")
st.caption("Upload real SEO & Google Analytics data → Ask business questions")

# =========================
# Safe CSV Loader
# =========================
def safe_read_csv(uploaded_file):
    try:
        return pd.read_csv(uploaded_file)
    except Exception:
        return pd.read_csv(
            uploaded_file,
            sep=",",
            engine="python",
            on_bad_lines="skip"
        )

# =========================
# Sidebar Upload
# =========================
st.sidebar.header("📥 Upload Data")

seo_file = st.sidebar.file_uploader(
    "SEO CSV (Search Console / Ahrefs / SEMrush)",
    type=["csv"]
)

analytics_file = st.sidebar.file_uploader(
    "Google Analytics CSV",
    type=["csv"]
)

# =========================
# Load Data
# =========================
seo_df = safe_read_csv(seo_file) if seo_file else None
analytics_df = safe_read_csv(analytics_file) if analytics_file else None

# =========================
# Preview
# =========================
if seo_df is not None:
    st.subheader("🔍 SEO Data Preview")
    st.success(f"Loaded {seo_df.shape[0]} rows × {seo_df.shape[1]} columns")
    st.dataframe(seo_df.head())

if analytics_df is not None:
    st.subheader("📈 Analytics Data Preview")
    st.success(f"Loaded {analytics_df.shape[0]} rows × {analytics_df.shape[1]} columns")
    st.dataframe(analytics_df.head())

# =========================
# Charts (FIXED)
# =========================
if analytics_df is not None:
    st.subheader("📊 Performance Charts")

    df = analytics_df.copy().reset_index(drop=True)

    numeric_cols = df.select_dtypes(include="number").columns.tolist()

    if len(numeric_cols) >= 1:
        col1, col2 = st.columns(2)

        with col1:
            st.markdown(f"**Trend – {numeric_cols[0]}**")
            chart_df = df[[numeric_cols[0]]].copy()
            chart_df["row"] = chart_df.index
            st.line_chart(chart_df.set_index("row"))

        if len(numeric_cols) > 1:
            with col2:
                st.markdown(f"**Trend – {numeric_cols[1]}**")
                chart_df = df[[numeric_cols[1]]].copy()
                chart_df["row"] = chart_df.index
                st.line_chart(chart_df.set_index("row"))
    else:
        st.warning("No numeric columns found for visualization.")

# =========================
# RAG Question Interface
# =========================
st.subheader("🤖 Ask MarketMind")

question = st.text_area(
    "Ask a business question",
    placeholder="How can I reduce CPA using SEO and analytics data?"
)

if st.button("🚀 Analyze"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Analyzing with MarketMind..."):
            try:
                response = requests.post(
                    API_URL,
                    json={"question": question},
                    timeout=120
                )

                if response.status_code == 200:
                    data = response.json()

                    st.success("Analysis Complete")

                    st.markdown("### 🧠 Executive Summary")
                    st.write(data.get("summary", "N/A"))

                    st.markdown("### 🔑 Key Insights")
                    for item in data.get("key_insights", []):
                        st.write("•", item)

                    st.markdown("### ✅ Recommendations")
                    for item in data.get("recommendations", []):
                        st.write("•", item)

                    st.markdown("### 📊 Expected Impact")
                    st.json(data.get("metrics_impact", {}))

                    st.markdown("### 🔍 Confidence Level")
                    st.info(data.get("confidence_level", "Unknown"))

                else:
                    st.error(f"API Error: {response.text}")

            except Exception as e:
                st.error(f"Connection error: {e}")

# =========================
# Export Placeholder
# =========================
st.subheader("📄 Export")
st.info("PDF / PPT export can be added next without backend changes.")
