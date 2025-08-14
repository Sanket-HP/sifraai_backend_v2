
from fastapi import APIRouter
from app.services.utils import load_dataset
from sklearn.inspection import permutation_importance
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

router = APIRouter(prefix="/explain", tags=["Explainable AI (7)"])

@router.get("/permutation_importance")
def perm_importance(ds_id: str, target: str):
    df = load_dataset(ds_id).dropna(subset=[target])
    X = df.select_dtypes(exclude="object").drop(columns=[target], errors="ignore").fillna(0)
    y = df[target]
    Xtr, Xte, ytr, yte = train_test_split(X, y, random_state=42, test_size=0.2)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(Xtr, ytr)
    r = permutation_importance(model, Xte, yte, n_repeats=5, random_state=42)
    importances = sorted(zip(X.columns, r.importances_mean), key=lambda x: -x[1])
    return [{"feature": f, "importance": float(v)} for f, v in importances]
