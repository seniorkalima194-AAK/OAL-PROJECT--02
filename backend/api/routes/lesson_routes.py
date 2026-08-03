"""lesson_routes.py
Router for lesson-related API endpoints. Should include endpoints for listing and retrieving lessons.
"""

from fastapi import APIRouter, status
from backend.api.schemas import ResponseEnvelope, LessonCreateRequest, LessonUpdateRequest
from backend.api.schemas import ResponseEnvelope
from backend.api.models import LessonCreateRequest, LessonPutRequest, LessonPatchRequest


# All text, messages, and error definitions come exclusively from here
from backend.api.constants import (
    LESSON_NOT_FOUND_MSG,
    LESSON_CREATE_SUCCESS_MSG,
    LESSON_REPLACE_SUCCESS_MSG,
    LESSON_UPDATE_SUCCESS_MSG,
    LESSON_PLACEHOLDER_TITLE
)

router = APIRouter()

@router.get("", response_model=ResponseEnvelope)
async def list_lessons():
    return ResponseEnvelope(data=[])
@router.post("", response_model=ResponseEnvelope, status_code=status.HTTP_201_CREATED)
async def create_lesson(payload: LessonCreateRequest):
    return ResponseEnvelope(data={
        "title": payload.title,
        "message": LESSON_CREATE_SUCCESS_MSG.format(title=payload.title)
    })

@router.get("/{id}", response_model=ResponseEnvelope)
async def get_lesson(id: int):
    return ResponseEnvelope(data={
        "id": id, 
        "title": LESSON_PLACEHOLDER_TITLE
    })

@router.put("/{id}", response_model=ResponseEnvelope)
async def replace_lesson(id: int, payload: LessonPutRequest):
    return ResponseEnvelope(data={
        "id": id, 
        "message": LESSON_REPLACE_SUCCESS_MSG
    })

@router.patch("/{id}", response_model=ResponseEnvelope)
async def update_lesson(id: int, payload: LessonPatchRequest):
    return ResponseEnvelope(data={
        "id": id, 
        "message": LESSON_UPDATE_SUCCESS_MSG
    })

