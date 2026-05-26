from fastapi import APIRouter

from schemas.chat_schema import ChatRequest

from services.llm_service import generate_answer
from services.verifier_service import verify_answer
from services.retrieval_service import retrieve_sources

router = APIRouter()

@router.post("/chat")
def chat(request: ChatRequest):

    answer = generate_answer(
        request.question
    )

    verification = verify_answer(
        answer
    )

    sources = retrieve_sources(
        answer
    )

    return {
        "answer": answer,
        "verification": verification,
        "sources": sources
    }