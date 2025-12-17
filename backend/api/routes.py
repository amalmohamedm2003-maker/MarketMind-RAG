from fastapi import APIRouter, HTTPException
from api.schemas import AnalyzeRequest, AnalyzeResponse
from rag.growth_agent import GrowthAgent
from core.logging import get_logger

router = APIRouter()
logger = get_logger()

agent = GrowthAgent()

@router.post("/analyze")
def analyze(req: AnalyzeRequest):
    try:
        result = agent.analyze(req.question)
        return result

    except Exception as e:
        logger.exception("Analysis failed")
        return {
            "answer": "System temporarily unavailable. Please retry.",
            "faithfulness": 0.0,
            "sources_used": 0
        }
