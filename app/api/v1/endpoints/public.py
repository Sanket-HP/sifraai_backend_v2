
from fastapi import APIRouter, HTTPException
from app.core.registry import set_public, get_dataset

router = APIRouter(prefix="/public", tags=["Public Showcase (21)"])

@router.post("/set")
def set_pub(ds_id: str, is_public: bool = True):
    rec = set_public(ds_id, is_public)
    if not rec:
        raise HTTPException(404, "Dataset not found")
    return rec
