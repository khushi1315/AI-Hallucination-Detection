from fastapi import APIRouter

router = APIRouter()


@router.get("/history")
def history():
    """
    Placeholder — DB integration to be added in Phase 5.
    Returns empty list for now so frontend doesn't break.
    """
    return {"history": []}