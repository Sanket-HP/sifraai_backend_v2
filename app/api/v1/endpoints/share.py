
from fastapi import APIRouter
router = APIRouter(prefix="/share", tags=["Collaboration (16)"])

@router.get("/link")
def link(ds_id: str):
    return {"share_url": f"/api/v1/eda/summary?ds_id={ds_id}"}
