from typing import Any, Optional, List
from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
import uuid

class ResponseMeta(BaseModel):
    trace_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class ResponseEnvelope(BaseModel):
    data: Optional[Any] = None
    error: Optional[Any] = None
    meta: ResponseMeta = Field(default_factory=ResponseMeta)

class UserRegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8)
    role: str 

class UserLoginRequest(BaseModel):
    email: EmailStr
    password: str

class LessonCreateRequest(BaseModel):
    id: int
    title: str
    difficulty: str
    content_path: str


class LessonUpdateRequest(BaseModel):
    title: Optional[str] = None
    difficulty: Optional[str] = None
    content_path: Optional[str] = None
