# backend/app/api/users.py
from fastapi import APIRouter
from app.models.user_model import User

router = APIRouter()

@router.get("/users")
async def get_users():
    # Fetch users from the database (dummy response here)
    return {"users": []}
