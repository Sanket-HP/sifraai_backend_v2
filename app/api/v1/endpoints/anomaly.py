
from fastapi import APIRouter
from app.services.utils import load_dataset
from sklearn.ensemble import IsolationForest

router = APIRouter(prefix="/anomaly", tags=["Anomaly Detection (8)"])

@router.get("/isolation_forest")
def iso(ds_id: str):
    df = load_dataset(ds_id)
    num = df.select_dtypes(exclude="object").fillna(0)
    model = IsolationForest(random_state=42, contamination=0.05)
    preds = model.fit_predict(num)
    df_res = df.copy()
    df_res["anomaly"] = (preds == -1).astype(int)
    return {"anomaly_count": int(df_res["anomaly"].sum())}
