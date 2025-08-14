
from fastapi import APIRouter, UploadFile, File
from app.core.config import PLUGIN_DIR
from pathlib import Path

router = APIRouter(prefix="/plugins", tags=["Plugin System (14)"])

@router.post("/upload")
async def upload_plugin(file: UploadFile = File(...)):
    target = PLUGIN_DIR / file.filename
    target.write_bytes(await file.read())
    return {"message": "plugin_uploaded", "path": str(target)}

@router.get("/list")
def list_plugins():
    return {"plugins": [p.name for p in Path(PLUGIN_DIR).glob("*.py")]}
