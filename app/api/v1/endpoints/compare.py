
from fastapi import APIRouter, HTTPException
from app.services.utils import load_dataset
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, r2_score
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
import numpy as np

router = APIRouter(prefix="/compare", tags=["Model Compare (6)"])

@router.get("/baseline")
def baseline(ds_id: str, target: str):
    df = load_dataset(ds_id).dropna(subset=[target])
    X = df.drop(columns=[target])
    y = df[target]
    is_classification = y.dtype == "object" or y.nunique() <= 20
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42)

    res = {}
    if is_classification:
        for name, m in {"logreg": LogisticRegression(max_iter=1000), "rf": RandomForestClassifier(100)}.items():
            m.fit(Xtr.select_dtypes(exclude="object").fillna(0), ytr)
            yp = m.predict(Xte.select_dtypes(exclude="object").fillna(0))
            res[name] = {"accuracy": float(accuracy_score(yte, yp))}
    else:
        for name, m in {"linreg": LinearRegression(), "rf": RandomForestRegressor(100)}.items():
            m.fit(Xtr.select_dtypes(exclude="object").fillna(0), ytr)
            yp = m.predict(Xte.select_dtypes(exclude="object").fillna(0))
            res[name] = {"r2": float(r2_score(yte, yp))}
    return res
