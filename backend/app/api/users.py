# backend/app/api/users.py
from fastapi import APIRouter
from app.models.user_model import User

router = APIRouter()

@router.get("/users/")
async def read_users():
    users = User.objects.all()
    return [{"name": user.name, "email": user.email} for user in users]
