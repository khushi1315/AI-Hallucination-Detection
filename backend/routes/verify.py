from fastapi import APIRouter

router = APIRouter()

@router.post("/verify")
def verify():

    return {
        "message": "Verify endpoint working"
    }