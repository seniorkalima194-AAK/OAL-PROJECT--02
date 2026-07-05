"""auth_schema.py
Pydantic schemas for authentication requests (login/register).
"""
from pydantic import BaseModel, EmailStr, Field

#usajili wa mwanafunzi

class RegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)
    
# login ya mwanafunzi
class LoginRequest(BaseModel):
    email: EmailStr
    password: str

#response ya mwanafunzi
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




