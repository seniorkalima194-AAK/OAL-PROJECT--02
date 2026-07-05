from fastapi import APIRouter, Depends
from backend.api.schemas import ResponseEnvelope
from backend.api.dependencies.auth import get_current_user

router = APIRouter(dependencies=[Depends(get_current_user)])

@router.get("/{lesson_id}", response_model=ResponseEnvelope)
async def get_quiz(lesson_id: int):
    return ResponseEnvelope(data={"lesson_id": lesson_id, "questions": []})

@router.post("/{lesson_id}/submit", response_model=ResponseEnvelope)
async def submit_quiz(lesson_id: int, payload: dict):
    return ResponseEnvelope(data={"lesson_id": lesson_id, "score": 100.0, "passed": True, "answers": payload.answers})


