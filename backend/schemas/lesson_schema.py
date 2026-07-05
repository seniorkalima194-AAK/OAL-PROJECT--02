"""lesson_schema.py
Pydantic schema for lessons: id, title, content metadata.
"""
from typing import Optional, List
from pydantic import BaseModel

#responcs vipindi kwa mwanafunzi
class LessonResourceResponse(BaseModel):
    id: str
    title: str
    file_url: str
    file_type: Optional[str]

    class Config:
        from_attributes = True
        
#Taarifa za vipindi
class LessonResponse(BaseModel):
    id: str
    title: str
    slug: str
    content: Optional[str]
    video_url: Optional[str]
    duration_seconds: int
    order_index: int
    is_preview: bool
    resources: List[LessonResourceResponse] = []

    class Config:
        from_attributes = True

#kutengeneza vipindi kwa mwanafunzi
class LessonCreateRequest(BaseModel):
    title: str
    content: Optional[str] = None
    video_url: Optional[str] = None
    duration_seconds: int = 0
    order_index: int
    is_preview: bool = False

#maendeleo ya mwanafuzi
class ProgressUpdateRequest(BaseModel):
    progress_seconds: int



