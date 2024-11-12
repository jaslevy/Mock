# backend/app/api/profile.py
import json
from fastapi import APIRouter, HTTPException, Response
from pathlib import Path
import os
from app.models.user_model import User

router = APIRouter()

@router.get("/profile")
async def get_profile_data():
    # Define the path to the JSON file and log it for debugging
    json_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "match_profile_data.json")
    print(f"Looking for profile data at: {json_file_path}")  # Debugging line
    
    # Attempt to read the JSON file
    try:
        with open(json_file_path, "r") as file:
            profile_data = json.load(file)
        return profile_data
    except FileNotFoundError:
        print("Profile data not found at the specified path")  # Debugging line
        raise HTTPException(status_code=404, detail="Profile data not found")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Error decoding profile data")
    
@router.get("/api/profile/user")
async def get_user_profile_data():
    try:
        print("Retrieving user profile data from MongoDB...")
        user_profile_data = User.objects.first()  # Retrieve the first user profile data
        print("User profile data:", user_profile_data)
        if user_profile_data:
            html_content = f"""
            <html>
                <body>
                    <h1>User Profile</h1>
                    <p>Name: {user_profile_data.name}</p>
                    <p>Email: {user_profile_data.email}</p>
                    <p>Bio: {user_profile_data.bio}</p>
                </body>
            </html>
            """
            print("HTML content:", html_content)
            return Response(content=html_content, media_type="text/html")
        else:
            print("No user profile data found")
            raise HTTPException(status_code=404, detail="User profile data not found")
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail="Error retrieving user profile data")

# @router.get("/")
# async def get_profile_data():
#     profile_data_path = Path(__file__).parent.parent / "profile_data.json"
#     try:
#         with open(profile_data_path, "r") as file:
#             data = json.load(file)
#         return data
#     except FileNotFoundError:
#         raise HTTPException(status_code=404, detail="Profile data not found")
