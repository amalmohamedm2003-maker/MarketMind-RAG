from loguru import logger
import sys
import os

os.makedirs("logs", exist_ok=True)

logger.remove()
logger.add(
    sys.stdout,
    level="INFO"
)
logger.add(
    "logs/app.log",
    rotation="10 MB",
    level="INFO"
)

def get_logger():
    return logger
