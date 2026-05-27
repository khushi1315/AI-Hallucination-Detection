from fastapi import APIRouter
from schemas.chat_schema import ChatRequest
from services.llm_service import generate_answer
from services.verifier_service import verify_answer
from services.retrieval_service import retrieve_sources

router = APIRouter()

@router.post("/chat")
def chat(request: ChatRequest):
    # Pass both question AND history to the LLM
    answer = generate_answer(
        request.question,
        request.history      # NEW — pass history
    )

    verification = verify_answer(answer)
    sources = retrieve_sources(answer)

    return {
        "answer": answer,
        "verification": verification,
        "sources": sources
    }

@router.post("/generate-response")
def generate_response(request: ChatRequest):
    """
    Alias for /chat — same logic, different URL.
    Required by the project spec.
    """
    answer = generate_answer(
        request.question,
        request.history
    )
    verification = verify_answer(answer)
    sources = retrieve_sources(answer)

    return {
        "answer": answer,
        "verification": verification,
        "sources": sources
    }