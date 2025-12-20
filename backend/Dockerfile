# =========================
# MarketMind RAG Backend
# CPU-only | Production Safe
# =========================

FROM python:3.11-slim

# Prevent Python buffering
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Avoid CUDA installs
ENV CUDA_VISIBLE_DEVICES=""
ENV TRANSFORMERS_NO_ADVISORY_WARNINGS=1

WORKDIR /app

# System deps (FAISS + torch CPU safe)
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# -------------------------
# Install Python deps FIRST
# (better Docker caching)
# -------------------------
COPY requirements.txt .

# Upgrade pip first
RUN pip install --upgrade pip

# Install CPU-only torch explicitly
RUN pip install \
    torch==2.2.2 \
    --index-url https://download.pytorch.org/whl/cpu

# Install remaining deps (NO GPU)
RUN pip install --no-cache-dir -r requirements.txt

# -------------------------
# Copy application code
# -------------------------
COPY . .

# -------------------------
# Ensure FAISS index exists
# -------------------------
RUN test -f vectorstore/faiss_index/index.faiss || \
    (echo "❌ FAISS index missing" && exit 1)

# -------------------------
# Expose API port
# -------------------------
EXPOSE 8000

# -------------------------
# Start FastAPI
# -------------------------
CMD ["python", "run_api.py"]
