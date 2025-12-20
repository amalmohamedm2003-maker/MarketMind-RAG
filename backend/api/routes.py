from fastapi import APIRouter
from pydantic import BaseModel
from rag.growth_agent import GrowthAgent
from loguru import logger

router = APIRouter()
agent = GrowthAgent()

class Query(BaseModel):
    question: str

@router.post("/analyze")
def analyze(req: Query):
    logger.info(f"Query: {req.question}")
    return agent.analyze(req.question)
