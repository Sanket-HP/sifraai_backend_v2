
from fastapi import APIRouter
router = APIRouter(prefix="/datasource", tags=["Multi-Source Ingest (15)"])

@router.get("/supported")
def supported():
    return {"sources": ["csv_upload","google_sheets (soon)","databases (soon)","cloud_buckets (soon)"]}
