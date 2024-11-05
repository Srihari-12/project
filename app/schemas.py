# app/schemas.py
from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    username: str
    email: EmailStr

class FoodItemCreate(BaseModel):
    name: str
    quantity: int
    description: Optional[str] = None

class FoodItemResponse(BaseModel):
    name: str
    quantity: int
    description: Optional[str] = None
