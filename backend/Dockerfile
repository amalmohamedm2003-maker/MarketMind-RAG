FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# System deps
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install CPU-only torch FIRST (critical)
RUN pip install --no-cache-dir \
    torch==2.2.2 \
    --index-url https://download.pytorch.org/whl/cpu

# Copy requirements
COPY backend/requirements.txt .

# Install remaining deps
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend
COPY backend ./backend

# Ensure FAISS exists
RUN test -f backend/vectorstore/faiss_index/index.faiss

EXPOSE 8000

CMD ["python", "backend/run_api.py"]
