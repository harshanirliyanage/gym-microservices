# gateway/auth.py
from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from fastapi import HTTPException, status
from pydantic import BaseModel

# ── Secret Key ────────────────────────────────────────────
SECRET_KEY = "gymmanagementsecretkey2026sliit"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60  # 60 minutes

# ── Mock Users ─────────────────────────────────────────────
USERS_DB = {
    "admin": {
        "username": "admin",
        "plain_password": "admin123",
        "role": "admin"
    },
    "staff": {
        "username": "staff",
        "plain_password": "staff123",
        "role": "staff"
    }
}

# ── Pydantic Models ───────────────────────────────────────
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class UserLogin(BaseModel):
    username: str
    password: str

# ── Helper Functions ──────────────────────────────────────
def authenticate_user(username: str, password: str):
    user = USERS_DB.get(username)
    if not user:
        return False
    if password != user["plain_password"]:
        return False
    return user

def create_access_token(data: dict,
                        expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=60)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    return encoded_jwt

def verify_token(token: str):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or expired token",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # Clean token - remove Bearer if accidentally included
        if token.startswith("Bearer "):
            token = token[7:]

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        return username
    except JWTError as e:
        print(f"JWT Error: {e}")  # for debugging
        raise credentials_exception