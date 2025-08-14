
from fastapi import APIRouter
router = APIRouter(prefix="/nlq", tags=["Natural Language Query (10)"])

@router.get("/ask")
def ask(ds_id: str, q: str):
    # Placeholder: actual NLQ would require an LLM; here we return a helpful hint
    return {"answer": "NLQ is enabled in pro mode. Try filters like: 'sum of <col> by <group>'."}
