from pathlib import Path

from fastapi import FastAPI, HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse

from .health import router as health_router
from .flashcards import router as flashcard_router

version = Path(Path(__file__).absolute().parent, "../../VERSION").read_text()
prefix = "/api"

app = FastAPI(
    title="Electric Discourse",
    version=version,
    openapi_url=prefix,
    docs_url=f"{prefix}/docs",
    redoc_url=None,
)


@app.exception_handler(HTTPException)
async def g3_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"status": exc.status, "message": exc.message},
    )

app.include_router(health_router, prefix=prefix)
app.include_router(flashcard_router, prefix=prefix)
