"""constants.py
Core constants for the backend, e.g., default DB path and other literals.
"""

# ADAPTIVE LEARNING SYSTEM — System Constants
# Sync required with: frontend/utils/constants.js


# --- Roles ---
STUDENT_ROLE: str = "student"
ADMIN_ROLE: str = "admin"

# --- Difficulty Levels ---
DIFFICULTY_LEVELS: dict = {
    1: "Beginner",
    2: "Elementary",
    3: "Intermediate",
    4: "Advanced",
    5: "Expert"
}

# --- Adaptive Engine Thresholds ---
SCORE_THRESHOLD_LOW: int = 40
SCORE_THRESHOLD_HIGH: int = 75
SCORE_VERSION: int = 1

# --- Token ---
TOKEN_TYPE: str = "bearer"
TOKEN_EXPIRED_CODE: str = "TOKEN_EXPIRED"
TOKEN_INVALID_CODE: str = "TOKEN_INVALID"

# --- HTTP Response Messages ---
MSG_LOGIN_SUCCESS: str = "Login successful"
MSG_REGISTER_SUCCESS: str = "Registration successful"
MSG_LOGOUT_SUCCESS: str = "Logout successful"
MSG_NOT_FOUND: str = "Resource not found"
MSG_UNAUTHORIZED: str = "Authentication required"
MSG_FORBIDDEN: str = "You do not have permission to perform this action"
MSG_VALIDATION_ERROR: str = "Validation failed"

# --- Progress Status ---
PROGRESS_NOT_STARTED: str = "not_started"
PROGRESS_IN_PROGRESS: str = "in_progress"
PROGRESS_COMPLETED: str = "completed"

# --- File Upload ---
MAX_UPLOAD_SIZE_MB: int = 10
MAX_UPLOAD_SIZE_BYTES: int = MAX_UPLOAD_SIZE_MB * 1024 * 1024
ALLOWED_IMAGE_TYPES: list = ["image/jpeg", "image/png", "image/gif"]
ALLOWED_DOCUMENT_TYPES: list = ["application/pdf"]
ALLOWED_VIDEO_TYPES: list = ["video/mp4", "video/mpeg"]

# --- Pagination ---
DEFAULT_PAGE_SIZE: int = 10
MAX_PAGE_SIZE: int = 100

# --- Password ---
MIN_PASSWORD_LENGTH: int = 8
MAX_PASSWORD_LENGTH: int = 64

# --- Quiz ---
MIN_QUIZ_SCORE: int = 0
MAX_QUIZ_SCORE: int = 100
MIN_DIFFICULTY: int = 1
MAX_DIFFICULTY: int = 5