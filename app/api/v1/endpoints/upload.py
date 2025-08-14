
from fastapi import APIRouter, UploadFile, File, HTTPException
from pathlib import Path
from app.core.config import DATA_DIR
from app.core.registry import register_dataset, list_datasets

router = APIRouter(prefix="/upload", tags=["Upload (1)"])

@router.post("/csv")
async def upload_csv(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV supported in MVP")
    target = DATA_DIR / file.filename
    content = await file.read()
    target.write_bytes(content)
    rec = register_dataset(file.filename, target, meta={"size": len(content)})
    return {"message": "uploaded", "dataset": rec}

@router.get("/list")
def list_all():
    return list_datasets()
