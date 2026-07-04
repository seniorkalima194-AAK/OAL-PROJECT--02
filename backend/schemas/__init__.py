"""Schemas package"""


# ---------------------------------------------------------------------------
# Auth schemas
# ---------------------------------------------------------------------------
from .auth_schema import (
    AuthBaseSchema,
    RegisterSchema,
    LoginSchema,
    PasswordChangeSchema,
    TokenResponseSchema,
    AuthUserResponseSchema,
)

# ---------------------------------------------------------------------------
# Student schemas
# ---------------------------------------------------------------------------
from .student_schema import (
    StudentBaseSchema,
    StudentCreateSchema,
    StudentUpdateSchema,
    StudentResponseSchema,
)

# ---------------------------------------------------------------------------
# Lesson schemas
# ---------------------------------------------------------------------------
from .lesson_schema import (
    LessonBaseSchema,
    LessonCreateSchema,
    LessonUpdateSchema,
    LessonResponseSchema,
)

# ---------------------------------------------------------------------------
# Question schemas
# ---------------------------------------------------------------------------
from .question_schema import (
    QuestionType,
    QuestionBaseSchema,
    QuestionCreateSchema,
    QuestionUpdateSchema,
    QuestionResponseSchema,
    QuestionGradingSchema,
)

# ---------------------------------------------------------------------------
# Quiz schemas
# ---------------------------------------------------------------------------
from .quiz_schema import (
    QuizBaseSchema,
    QuizCreateSchema,
    QuizUpdateSchema,
    QuizResponseSchema,
    QuizSchema,
)

# ---------------------------------------------------------------------------
# Progress schemas
# ---------------------------------------------------------------------------
from .progress_schema import (
    ProgressStatus,
    ProgressBaseSchema,
    ProgressCreateSchema,
    ProgressUpdateSchema,
    ProgressResponseSchema,
)

__all__ = [
    # Auth
    "AuthBaseSchema",
    "RegisterSchema",
    "LoginSchema",
    "PasswordChangeSchema",
    "TokenResponseSchema",
    "AuthUserResponseSchema",
    # Student
    "StudentBaseSchema",
    "StudentCreateSchema",
    "StudentUpdateSchema",
    "StudentResponseSchema",
    # Lesson
    "LessonBaseSchema",
    "LessonCreateSchema",
    "LessonUpdateSchema",
    "LessonResponseSchema",
    # Question
    "QuestionType",
    "QuestionBaseSchema",
    "QuestionCreateSchema",
    "QuestionUpdateSchema",
    "QuestionResponseSchema",
    "QuestionGradingSchema",
    # Quiz
    "QuizBaseSchema",
    "QuizCreateSchema",
    "QuizUpdateSchema",
    "QuizResponseSchema",
    "QuizSchema",
    # Progress
    "ProgressStatus",
    "ProgressBaseSchema",
    "ProgressCreateSchema",
    "ProgressUpdateSchema",
    "ProgressResponseSchema",
]