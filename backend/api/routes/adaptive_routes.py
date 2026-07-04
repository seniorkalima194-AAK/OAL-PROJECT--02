from fastapi import APIRouter, Depends, Query
from backend.api.schemas import ResponseEnvelope
from backend.api.dependencies.auth import get_current_user

router = APIRouter(dependencies=[Depends(get_current_user)])

@router.get("/next-lesson", response_model=ResponseEnvelope)
async def get_next_lesson(student_id: int = Query(..., description="ID of the student")):
    return ResponseEnvelope(data={"student_id": student_id, "recommended_lesson_id": 2, "reason": "Threshold rule baseline"})
