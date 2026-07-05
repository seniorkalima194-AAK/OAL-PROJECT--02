from fastapi import APIRouter
from backend.api.schemas import ResponseEnvelope, LessonCreateRequest, LessonUpdateRequest

router = APIRouter()

@router.get("", response_model=ResponseEnvelope)
async def list_lessons():
    return ResponseEnvelope(data=[])

@router.post("", response_model=ResponseEnvelope)
async def create_lesson(payload: LessonCreateRequest):
    return ResponseEnvelope(data={"message": f"Lesson '{payload.title}' created successfully"})

@router.get("/{id}", response_model=ResponseEnvelope)
async def get_lesson(id: int):
    return ResponseEnvelope(data={"id": id, "title": "Lesson Content Placeholder"}) 

@router.put("/{id}", response_model=ResponseEnvelope)
async def replace_lesson(id: int, payload: LessonUpdateRequest): 
    return ResponseEnvelope(data={"id": id, "message": "Lesson fully replaced"}) 

@router.patch("/{id}", response_model=ResponseEnvelope)
async def update_lesson(id: int, payload: LessonUpdateRequest):   
    return ResponseEnvelope(data={"message": f"Lesson {id} updated"})

@router.delete("/{id}", response_model=ResponseEnvelope)
async def delete_lesson(id: int):
    return ResponseEnvelope(data={"id": id, "status": "deleted"})
