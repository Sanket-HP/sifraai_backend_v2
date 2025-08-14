
from fastapi import APIRouter
from app.core.registry import list_datasets

router = APIRouter(prefix="/versioning", tags=["Versioning (20)"])

@router.get("/datasets")
def datasets():
    return list_datasets()
