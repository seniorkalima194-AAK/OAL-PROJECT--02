"""progress_schema.py
Pydantic schema for progress payloads and responses.
"""
from datetime import date as date_type
from typing import Optional
from pydantic import BaseModel

class CourseProgressResponse(BaseModel):
    course_id: str
    total_lessons: int
    completed_lessons: int
    completion_percent: float
    total_time_spent_seconds: int
    status: str
    started_at: Optional[str]
    completed_at: Optional[str]

    class Config:
        from_attributes = True

class StreakResponse(BaseModel):
    current_streak_days: int
    longest_streak_days: int
    last_activity_date: Optional[date_type]

    class Config:
        from_attributes = True

class AchievementResponse(BaseModel):
    code: str
    title: str
    description: Optional[str]
    icon_url: Optional[str]
    earned_at: str

