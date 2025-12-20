from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="MarketMind RAG")
app.include_router(router)
