
from fastapi import APIRouter, Depends, HTTPException
from ..schemas import FoodItemCreate, FoodItemResponse
from ..crud import create_food_item

router = APIRouter()

@router.post("/items", response_model=FoodItemResponse)
async def add_food_item(food_item: FoodItemCreate):
    return await create_food_item(food_item)
