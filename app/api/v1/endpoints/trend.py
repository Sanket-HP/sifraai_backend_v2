
from fastapi import APIRouter
from app.services.utils import load_dataset
import pandas as pd

router = APIRouter(prefix="/trend", tags=["Trend Analysis (24)"])

@router.get("/moving_trend")
def moving_trend(ds_id: str, date_col: str, target: str, window: int = 7):
    df = load_dataset(ds_id)
    df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
    ts = df[[date_col, target]].dropna().sort_values(date_col).set_index(date_col)[target]
    trend = ts.rolling(window=window, min_periods=1).mean()
    return {"trend": [float(x) for x in trend.values]}
