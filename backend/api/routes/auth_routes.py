from fastapi import APIRouter, status
from backend.api.schemas import (
    UserLoginRequest,
    UserRegisterRequest,
    ResponseEnvelope,
)

router = APIRouter()

@router.post("/register", response_model=ResponseEnvelope, status_code=status.HTTP_201_CREATED)
async def register(payload: UserRegisterRequest):
    return ResponseEnvelope(data={"message": f"Registration successful for {payload.email}"})

@router.post("/login", response_model=ResponseEnvelope)
async def login(payload: UserLoginRequest):
    return ResponseEnvelope(data={"access_token": "mock_jwt_token", "token_type": "bearer"})

