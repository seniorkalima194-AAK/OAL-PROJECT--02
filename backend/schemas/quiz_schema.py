"""quiz_schema.py
Pydantic schema for quizzes and metadata.
"""
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel
from .question_schema import OptionResponse, QuestionResponse, QuestionResultResponse

class DifficultyLevelEnum(str, Enum):
    easy = "easy"
    medium = "medium"
    hard = "hard"

class QuestionResponse(BaseModel):
    id: str
    question_text: str
    question_type: str
    difficulty_level: DifficultyLevelEnum
    points: int
    order_index: int
    image_url: Optional[str]
    options: List[OptionResponse] = []

    class Config:
        from_attributes = True

class QuizResponse(BaseModel):
    id: str
    title: str
    description: Optional[str]
    passing_score_percent: float
    time_limit_seconds: Optional[int]
    use_random_selection: bool
    easy_question_count: int
    medium_question_count: int
    hard_question_count: int
    questions: List[QuestionResponse] = []

    class Config:
        from_attributes = True

class QuestionCreateRequest(BaseModel):
    question_text: str
    question_type: str
    difficulty_level: DifficultyLevelEnum = DifficultyLevelEnum.medium
    points: Optional[int] = None  # kama None, tumia auto_assign_points()
    order_index: int

class DifficultyBreakdown(BaseModel):
    easy: int
    medium: int
    hard: int

class QuizResultResponse(BaseModel):
    attempt_id: str
    score_percent: float
    is_passed: bool
    total_points: int
    points_earned: float
    difficulty_breakdown: DifficultyBreakdown
    question_results: List[QuestionResultResponse]

