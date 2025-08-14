
from fastapi import APIRouter, HTTPException
from app.services.utils import load_dataset
from app.core.registry import register_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, r2_score
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
import pandas as pd
import numpy as np

router = APIRouter(prefix="/automl", tags=["AutoML (5)"])

@router.post("/train")
def train(ds_id: str, target: str):
    df = load_dataset(ds_id).dropna(subset=[target])
    if target not in df.columns:
        raise HTTPException(status_code=400, detail="Target column not found")
    X = df.drop(columns=[target])
    y = df[target]
    cat_cols = X.select_dtypes(include=["object","category"]).columns.tolist()
    num_cols = X.select_dtypes(exclude=["object","category"]).columns.tolist()

    is_classification = y.dtype == "object" or y.nunique() <= 20
    pre = ColumnTransformer([
        ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols)
    ], remainder="passthrough")

    if is_classification:
        model = RandomForestClassifier(n_estimators=100, random_state=42)
    else:
        model = RandomForestRegressor(n_estimators=100, random_state=42)

    pipe = Pipeline([("prep", pre), ("model", model)])
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42)
    pipe.fit(Xtr, ytr)
    yp = pipe.predict(Xte)

    if is_classification:
        metric = {"accuracy": float(accuracy_score(yte, yp))}
    else:
        metric = {"r2": float(r2_score(yte, yp))}
    rec = register_model("automl_rf", ds_id, metric)
    return {"model": rec, "metrics": metric}
