
from fastapi import APIRouter
router = APIRouter(prefix="/chat", tags=["AI Analyst Chat (18)"])

@router.post("/ask")
def ask(message: str):
    return {"reply": "I'm a stub analyst: please provide dataset id and goal for deeper help."}
