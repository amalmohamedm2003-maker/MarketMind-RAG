FROM python:3.11-slim

WORKDIR /app

# System dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip (IMPORTANT for Python 3.11)
RUN pip install --upgrade pip

# 1️⃣ Install CPU-only PyTorch from PyTorch index
RUN pip install --no-cache-dir \
    --index-url https://download.pytorch.org/whl/cpu \
    torch==2.2.2

# 2️⃣ Reset pip back to PyPI explicitly
RUN pip config unset global.index-url || true

# Copy requirements
COPY requirements.txt .

# 3️⃣ Install remaining dependencies from PyPI
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Copy FAISS index
COPY vectorstore ./vectorstore

ENV PYTHONPATH=/app

EXPOSE 8000

CMD ["python", "run_api.py"]
