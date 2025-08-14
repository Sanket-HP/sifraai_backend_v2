
from fastapi import APIRouter
from app.services.utils import load_dataset
from app.core.config import REPORT_DIR
import uuid

router = APIRouter(prefix="/report", tags=["Report Export (11)"])

@router.post("/html")
def export_html(ds_id: str):
    df = load_dataset(ds_id)
    html = f"""<html><body><h1>Sifra AI Report</h1><p>Rows: {df.shape[0]}, Cols: {df.shape[1]}</p>{df.head(20).to_html()}</body></html>"""
    name = f"report_{uuid.uuid4().hex}.html"
    path = REPORT_DIR / name
    path.write_text(html, encoding="utf-8")
    return {"message": "report_ready", "path": str(path)}
