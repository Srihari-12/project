# app/routes/auth_routes.py
from fastapi import APIRouter, Depends, HTTPException, status
from datetime import timedelta
from ..schemas import UserCreate, UserResponse
from ..auth import authenticate_user, create_access_token
from ..crud import create_user

router = APIRouter()

@router.post("/signup", response_model=UserResponse)
async def signup(user: UserCreate):
    existing_user = await db.users.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return await create_user(user)

@router.post("/login")
async def login(username: str, password: str):
    user = await authenticate_user(username, password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
