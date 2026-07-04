from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from backend.api.router import api_router

app = FastAPI(
    title="Offline Learning System API",
)

app.include_router(api_router, prefix="/api")

@app.exception_handler(status.HTTP_405_METHOD_NOT_ALLOWED)
async def method_not_allowed_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
        content={
            "data": None,
            "error": f"Method {request.method} Not Allowed on this route.",
            "meta": {}
        }
    )