# users.py

from fastapi import APIRouter, HTTPException
from typing import List
from models.good import User, CreateUser

router = APIRouter()

# база данных
db_users = [
    {"id": 1, "username": "user1", "email": "user1@example.com"},
    {"id": 2, "username": "user2", "email": "user2@example.com"},
]

@router.get("/users", response_model=List[User])
async def get_users():
    return db_users

@router.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    user = next((u for u in db_users if u["id"] == user_id), None)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")

@router.post("/users", response_model=User)
async def create_user(user: CreateUser):
    new_user = {"id": len(db_users) + 1, **user.dict()}
    db_users.append(new_user)
    return new_user

@router.put("/users", response_model=User)
async def edit_user(user_id: int, updated_user: CreateUser):
    user_index = next((index for index, u in enumerate(db_users) if u["id"] == user_id), None)
    if user_index is not None:
        db_users[user_index].update({"username": updated_user.username, "email": updated_user.email})
        return db_users[user_index]
    raise HTTPException(status_code=404, detail="User not found")

@router.delete("/users/{user_id}", response_model=User)
async def delete_user(user_id: int):
    user_index = next((index for index, u in enumerate(db_users) if u["id"] == user_id), None)
    if user_index is not None:
        return db_users.pop(user_index)
    raise HTTPException(status_code=404, detail="User not found")

