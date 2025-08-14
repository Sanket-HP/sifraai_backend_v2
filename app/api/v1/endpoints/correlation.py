
from fastapi import APIRouter
from app.services.utils import load_dataset

router = APIRouter(prefix="/correlation", tags=["Correlation Finder (23)"])

@router.get("/matrix")
def matrix(ds_id: str):
    df = load_dataset(ds_id)
    num = df.select_dtypes(exclude="object")
    corr = num.corr(numeric_only=True).fillna(0.0)
    return {"columns": corr.columns.tolist(), "matrix": corr.values.tolist()}
