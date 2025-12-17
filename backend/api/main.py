from fastapi import FastAPI
from api.routes import router
from core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def health_check():
    return {
        "status": "ok",
        "service": settings.PROJECT_NAME
    }
