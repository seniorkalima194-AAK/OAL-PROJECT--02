"""middleware.py
Application-level middleware definitions and helpers.
"""

from fastapi import FastAPI

from middleware.request_logger import RequestLoggerMiddleware
from middleware.auth import AuthMiddleware
from middleware.permissions import PermissionsMiddleware

def register_middleware(app: FastAPI) -> None:
    """
    This middleware is applied in REVERSE of registration order
    (last added = first to run). Registered here so ordering is explicit
    and auditable in one place. (Order matters)
    """
    app.add_middleware(PermissionsMiddleware)   # runs 3rd
    app.add_middleware(AuthMiddleware)          # runs 2nd
    app.add_middleware(RequestLoggerMiddleware) # runs 1st


