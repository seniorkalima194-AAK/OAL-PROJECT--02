"""API routes package"""

from . import auth_routes, lesson_routes, quiz_routes, progress_routes, adaptive_routes

__all__ = [
    "auth_routes",
    "lesson_routes",
    "quiz_routes",
    "progress_routes",
    "adaptive_routes",
]
