
from fastapi import APIRouter
from app.services.utils import load_dataset
from app.core.config import DATA_DIR
import hashlib

router = APIRouter(prefix="/anonymize", tags=["Anonymization (4)"])

@router.post("/hash")
def hash_columns(ds_id: str, cols: str):
    df = load_dataset(ds_id)
    targets = [c.strip() for c in cols.split(",") if c.strip() in df.columns]
    for c in targets:
        df[c] = df[c].astype(str).apply(lambda x: hashlib.sha256(x.encode()).hexdigest())
    out_path = DATA_DIR / f"anon_{ds_id}.csv"
    df.to_csv(out_path, index=False)
    return {"message": "anonymized", "path": str(out_path)}
