
from fastapi import APIRouter
from app.services.utils import load_dataset
import pandas as pd

router = APIRouter(prefix="/forecast", tags=["Simple Forecast (9)"])

@router.get("/moving_average")
def moving_avg(ds_id: str, date_col: str, target: str, window: int = 7, horizon: int = 7):
    df = load_dataset(ds_id)
    df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
    ts = df[[date_col, target]].dropna().sort_values(date_col).set_index(date_col)[target]
    ma = ts.rolling(window=window, min_periods=1).mean()
    last = ma.iloc[-1] if len(ma) else 0.0
    future = [float(last) for _ in range(horizon)]
    return {"last_ma": float(last), "forecast": future}
