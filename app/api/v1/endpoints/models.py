
from fastapi import APIRouter
from app.core.registry import list_models

router = APIRouter(prefix="/models", tags=["Model Registry (22)"])

@router.get("/list")
def list_all():
    return list_models()
