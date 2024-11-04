# backend/app/api/profile.py
import json
from fastapi import APIRouter, HTTPException
from pathlib import Path

router = APIRouter()

@router.get("/")
async def get_profile_data():
    profile_data_path = Path(__file__).parent.parent / "profile_data.json"
    try:
        with open(profile_data_path, "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Profile data not found")
