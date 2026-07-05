from fastapi import APIRouter

from backend.api.routes.auth_routes import router as auth_router
from backend.api.routes.lesson_routes import router as lesson_router
from backend.api.routes.quiz_routes import router as quiz_router
from backend.api.routes.progress_routes import router as progress_router
from backend.api.routes.adaptive_routes import router as adaptive_router

api_router = APIRouter()

api_router.include_router(auth_router, prefix="/auth", tags=["Authentication"])
api_router.include_router(lesson_router, prefix="/lessons", tags=["Lessons"])
api_router.include_router(quiz_router, prefix="/quizzes", tags=["Quizzes"])
api_router.include_router(progress_router, prefix="/progress", tags=["Progress"])
api_router.include_router(adaptive_router, prefix="/adaptive", tags=["Adaptive"])
