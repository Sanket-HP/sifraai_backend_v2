
from fastapi import APIRouter
from app.services.utils import load_dataset

router = APIRouter(prefix="/quality", tags=["Data Quality Score (3)"])

@router.get("/score")
def score(ds_id: str):
    df = load_dataset(ds_id)
    rows, cols = df.shape
    missing = df.isna().sum().sum()
    unique_cols = sum(df.nunique() > 1)
    score = max(0, 100 - (missing / max(1, rows*cols))*100 + (unique_cols/cols)*10)
    return {"rows": rows, "cols": cols, "missing_cells": int(missing), "score": round(score,2)}
