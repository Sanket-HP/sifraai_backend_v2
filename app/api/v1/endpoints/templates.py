
from fastapi import APIRouter
router = APIRouter(prefix="/templates", tags=["Project Templates (17)"])

@router.get("/list")
def list_templates():
    return {"templates": ["sales_analysis","sentiment_analysis","fraud_detection","churn_prediction"]}
