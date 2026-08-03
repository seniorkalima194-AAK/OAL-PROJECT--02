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



from fastapi import APIRouter, status, Depends, HTTPException
from typing import Any

# canonical response wrapper used across the API
from backend.api.schemas import ResponseEnvelope, LessonUpdateRequest
# canonical lesson schemas (customer-facing) in repo
from backend.schemas.lesson_schema import LessonCreateRequest, LessonResponse
# auth dependency pattern used elsewhere in the project
from backend.api.dependencies.auth import get_current_user

from backend.api.constants import (
    LESSON_NOT_FOUND_MSG,
    LESSON_CREATE_SUCCESS_MSG,
    LESSON_REPLACE_SUCCESS_MSG,
    LESSON_UPDATE_SUCCESS_MSG,
    LESSON_PLACEHOLDER_TITLE
)

router = APIRouter()

@router.get("", response_model=ResponseEnvelope)
async def list_lessons() -> ResponseEnvelope:
    """
    List lessons.
    NOTE: Replace the empty list with a call to your service/repository, e.g.:
      lessons = LessonService.list_all()
    """
    return ResponseEnvelope(data=[])

@router.post(
    "",
    response_model=ResponseEnvelope,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(get_current_user)],
)
async def create_lesson(payload: LessonCreateRequest) -> ResponseEnvelope:
    """
    Create a lesson.
    TODO: Call your LessonService to persist and return the created object.
    """
    # placeholder response until service layer is integrated
    created = {
        "id": 1,
        "title": payload.title,
        "message": LESSON_CREATE_SUCCESS_MSG.format(title=payload.title),
    }
    return ResponseEnvelope(data=created)

@router.get("/{id}", response_model=ResponseEnvelope)
async def get_lesson(id: int) -> ResponseEnvelope:
    """
    Retrieve a lesson by id.
    TODO: Replace the placeholder with: lesson = LessonService.get_by_id(id)
    """
    # Example guard; replace with real lookup
    if id <= 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            details=LESSON_NOT_FOUND_MSG>format(id=id)
        )
    # placeholder payload until real data is returned
    return ResponseEnvelope(data={"id": id, "title": LESSON_PLACEHOLDER_TITLE})

@router.put("/{id}", response_model=ResponseEnvelope, dependencies=[Depends(get_current_user)])
async def replace_lesson(id: int, payload: LessonCreateRequest) -> ResponseEnvelope:
    # TODO: Call LessonService.replace(id, payload)
    return ResponseEnvelope(data={"id": id, "message": LESSON_REPLACE_SUCCESS_MSG})

@router.patch("/{id}", response_model=ResponseEnvelope, dependencies=[Depends(get_current_user)])
async def update_lesson(id: int, payload: LessonUpdateRequest) -> ResponseEnvelope:
    # TODO: Call LessonService.update(id, payload)
    return ResponseEnvelope(data={"id": id, "message": LESSON_UPDATE_SUCCESS_MSG})
