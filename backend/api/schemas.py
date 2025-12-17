from pydantic import BaseModel, Field

class AnalyzeRequest(BaseModel):
    question: str = Field(
        ...,
        example="How can I reduce CPA in paid search campaigns?"
    )

class AnalyzeResponse(BaseModel):
    question: str
    answer: str
    sources_used: int
