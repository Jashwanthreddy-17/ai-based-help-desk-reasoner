from fastapi import APIRouter
from pydantic import BaseModel

from backend.ai.co6_hybrid import HybridReasoner

router = APIRouter(
    prefix="/chat",
    tags=["AI Chat"]
)

reasoner = HybridReasoner()


class ChatRequest(BaseModel):

    query: str


@router.post("/")
def chat(request: ChatRequest):

    result = reasoner.reason(
        request.query
    )

    return result