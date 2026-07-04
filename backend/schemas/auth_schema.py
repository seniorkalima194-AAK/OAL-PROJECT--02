"""auth_schema.py
Pydantic schemas for authentication requests (login/register).
"""
from pydantic import BaseModel, EmailStr, Field

class RegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int

class UserResponse(BaseModel):
    id: str
    email: str
    email_verified: bool

    class Config:
        from_attributes = True




