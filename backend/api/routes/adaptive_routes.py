#this is adaptive routes api where one can Update get_next_lesson to use RecommendationService
from fastapi import APIRouter, Depends, Query
from backend.api.schemas import ResponseEnvelope
from backend.api.dependencies.auth import get_current_user
from backend.services.recommendation_service import RecommendationService

router = APIRouter(dependencies=[Depends(get_current_user)])

@router.get("/next-lesson", response_model=ResponseEnvelope)
async def get_next_lesson(student_id: int = Query(..., description="ID of the student")):
    recommendation = RecommendationService.get_next_lesson_recommendation(student_id)
    return ResponseEnvelope(data=recommendation)
   
