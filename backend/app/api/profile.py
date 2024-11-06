# backend/app/api/profile.py
import json
from fastapi import APIRouter, HTTPException
from pathlib import Path
import os

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
    
@router.get("/profile/user")
async def get_user_profile_data():
    json_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "profile_data.json")
    try:
        with open(json_file_path, "r") as file:
            user_profile_data = json.load(file)
        return user_profile_data
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="User profile data not found")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Error decoding user profile data")

# @router.get("/")
# async def get_profile_data():
#     profile_data_path = Path(__file__).parent.parent / "profile_data.json"
#     try:
#         with open(profile_data_path, "r") as file:
#             data = json.load(file)
#         return data
#     except FileNotFoundError:
#         raise HTTPException(status_code=404, detail="Profile data not found")
