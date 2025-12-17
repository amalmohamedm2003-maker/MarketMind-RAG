# MarketMind AI – Growth Intelligence RAG

## Overview
MarketMind AI is a production-grade Retrieval-Augmented Generation (RAG) system
designed to generate actionable digital marketing growth strategies.

## Features
- Multi-source marketing data ingestion
- FAISS-based semantic retrieval
- Gemini + local CPU LLM routing
- Fault-tolerant inference
- FastAPI service
- Accuracy & relevance evaluation

## Architecture
- Data pipelines → Vector DB → RAG → LLM Router → API

## Why this project is different
- Strategy-focused outputs (not chat)
- Cost-aware & quota-safe
- Production-ready API
- Evaluation-driven RAG

## How to run
```bash
python run_api.py
