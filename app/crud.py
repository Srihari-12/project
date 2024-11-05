# app/crud.py
from .database import db
from .models import User, FoodItem
from .auth import get_password_hash

async def create_user(user):
    user_data = {
        "username": user.username,
        "email": user.email,
        "hashed_password": get_password_hash(user.password),
    }
    new_user = await db.users.insert_one(user_data)
    return await db.users.find_one({"_id": new_user.inserted_id})

async def create_food_item(food_item):
    new_item = await db.inventory.insert_one(food_item.dict())
    return await db.inventory.find_one({"_id": new_item.inserted_id})
