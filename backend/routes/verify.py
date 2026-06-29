from fastapi import APIRouter
from pydantic import BaseModel
from services.verifier_service import verify_answer

router = APIRouter()


class VerifyRequest(BaseModel):
    answer: str


@router.post("/verify")
def verify(request: VerifyRequest):
    result = verify_answer(request.answer)
    return result