
from fastapi import APIRouter
router = APIRouter(prefix="/pipeline", tags=["Pipeline Builder (13)"])

@router.get("/blueprint")
def blueprint():
    return {"stages": ["ingest","clean","feature","train","evaluate","deploy"]}
