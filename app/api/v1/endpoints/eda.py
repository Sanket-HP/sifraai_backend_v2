
from fastapi import APIRouter, HTTPException, Query
from app.services.utils import load_dataset
import pandas as pd

router = APIRouter(prefix="/eda", tags=["Auto EDA (2)"])

@router.get("/summary")
def summary(ds_id: str):
    df = load_dataset(ds_id)
    desc = df.describe(include="all").fillna("").to_dict()
    missing = df.isna().mean().to_dict()
    columns = df.dtypes.astype(str).to_dict()
    return {"shape": df.shape, "columns": columns, "missing_ratio": missing, "describe": desc}
