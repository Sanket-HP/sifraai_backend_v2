
from fastapi import APIRouter
router = APIRouter(prefix="/bi", tags=["BI Export (19)"])

@router.get("/powerbi")
def powerbi_stub(ds_id: str):
    return {"export": "Power BI export link (stub)"}
