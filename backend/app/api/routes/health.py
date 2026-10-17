from fastapi import APIRouter
from app.core.config import settings

router = APIRouter(prefix="/health", tags=["health"])


@router.get("")
def health():
    return {"status": "healthy", "version": "0.1.0", "environment": settings.environment, "demo_mode": settings.demo_mode}
