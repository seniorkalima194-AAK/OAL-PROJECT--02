from fastapi import Depends, HTTPException, status, Request

async def get_current_user(request: Request) -> dict:
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing or invalid credentials"
        )
    
    token = auth_header.split(" ")[1]
    # In a later issue, decode the token here using your core security modules
    return {"user_id": 1, "role": "student"}

async def get_admin_user(current_user: dict = Depends(get_current_user)) -> dict:
    if current_user.get("role") != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Insufficient role permissions"
        )
    return current_user