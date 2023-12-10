from fastapi import APIRouter, HTTPException


router = APIRouter()


@router.get(
    "/health",
    tags=["health"],
    status_code=200,
)
def health_check():
    """Unauthenticated health check."""
    try:
        return {"message": "success"}
    except Exception as e:
        response = {"status": "fail", "message": "Health check failed."}
        raise HTTPException(status_code=400, **response)
