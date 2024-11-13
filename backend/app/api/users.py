from fastapi import APIRouter, HTTPException
from app.models.user_model import User

from mongoengine import connect, Document, StringField, EmailField, ListField, FloatField, IntField, DateTimeField
from datetime import datetime

# Connect to MongoDB (you can also put this in a separate db module)
# connect(
#     host="mongodb+srv://jl4537:mongo123@mockcluster.skhaw.mongodb.net/mock_interview_platform?retryWrites=true&w=majority&tlsAllowInvalidCertificates=true"
# )

# Define the User model

# Initialize router
router = APIRouter()

@router.get("/")
async def read_users():
    try:
        # Fetch all users from the database
        users = User.objects()  # This will return all users from the 'users' collection

        if not users:
            raise HTTPException(status_code=404, detail="No users found in the database.")
        
        # Return users in a simplified format
        return [
            {
                "name": f"{user.first_name} {user.last_name}",
                "email": user.email,
                "bio": user.bio
            }
            for user in users
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching users: {str(e)}")
