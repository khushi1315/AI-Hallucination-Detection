from fastapi import APIRouter

router = APIRouter()

@router.get("/history")
def history():

    return {
        "message": "History endpoint working"
    }