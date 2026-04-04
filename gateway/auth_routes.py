# gateway/auth_routes.py
from fastapi import APIRouter, HTTPException, status
from datetime import timedelta
from auth import (
    authenticate_user,
    create_access_token,
    UserLogin,
    Token,
    ACCESS_TOKEN_EXPIRE_MINUTES
)

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/login", response_model=Token)
def login(user: UserLogin):
    """Login and get JWT token"""
    authenticated = authenticate_user(
        user.username, user.password
    )
    if not authenticated:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    access_token = create_access_token(
        data={"sub": authenticated["username"]},
        expires_delta=timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )
    )
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

@router.get("/verify")
def verify_token_route(token: str):
    """Verify if token is valid"""
    from auth import verify_token
    username = verify_token(token)
    return {
        "valid": True,
        "username": username
    }