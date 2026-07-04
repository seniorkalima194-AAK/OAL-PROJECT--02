"""student_schema.py
Pydantic schema for Student input/output validation.
"""
from datetime import date as date_type, time as time_type
from typing import Optional, List
from pydantic import BaseModel, EmailStr


class GuardianCreate(BaseModel):
    full_name: str
    relationship_type: Optional[str] = None
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None
    is_primary: bool = True


class GuardianResponse(GuardianCreate):
    id: str

    class Config:
        from_attributes = True


class StudentCreateRequest(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: Optional[date_type] = None
    phone_number: Optional[str] = None
    country: Optional[str] = None
    education_level: Optional[str] = None
    guardian: Optional[GuardianCreate] = None  # lazima kama ni mtoto


class StudentUpdateRequest(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone_number: Optional[str] = None
    avatar_url: Optional[str] = None
    country: Optional[str] = None
    education_level: Optional[str] = None


class StudentResponse(BaseModel):
    id: str
    user_id: str
    first_name: str
    last_name: str
    full_name: str
    date_of_birth: Optional[date_type]
    avatar_url: Optional[str]
    country: Optional[str]
    education_level: Optional[str]
    guardians: List[GuardianResponse] = []

    class Config:
        from_attributes = True


class StudentPreferenceUpdate(BaseModel):
    email_notifications: Optional[bool] = None
    reminder_notifications: Optional[bool] = None
    daily_reminder_time: Optional[time_type] = None
    weekly_goal_minutes: Optional[int] = None
    dark_mode: Optional[bool] = None


class StudentPreferenceResponse(BaseModel):
    email_notifications: bool
    reminder_notifications: bool
    daily_reminder_time: Optional[time_type]
    weekly_goal_minutes: int
    dark_mode: bool

    class Config:
        from_attributes = True


class EnrollmentResponse(BaseModel):
    id: str
    course_id: str
    enrolled_at: str
    completed_at: Optional[str]

    class Config:
        from_attributes = True
