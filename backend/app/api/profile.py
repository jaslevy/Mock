# backend/app/api/profile.py
from hashlib import sha1
import json
from fastapi import APIRouter, HTTPException, Response
from fastapi.requests import Request
from pathlib import Path
import os
from app.models.schedules_model import Schedule
from app.models.user_model import User  # Assuming you have a User model
from datetime import datetime
from pymongo.mongo_client import MongoClient


import logging

logger = logging.getLogger(__name__)


router = APIRouter()

# TODO: Abstract URI INTO MONGO_URI, currently here to prototype
# MONGO_URI = os.getenv("MONGO_URI")
MONGO_URI = "mongodb+srv://jl4537:mongo123@mockcluster.skhaw.mongodb.net/mock_interview_platform?retryWrites=true&w=majority&tlsAllowInvalidCertificates=true"

@router.get("/maindata")
async def get_match_data(request: Request):
    try:
        # Extract the user data (e.g., google_id) from the session
        user = request.session.get("user")
        if not user or "google_id" not in user:
            raise HTTPException(status_code=401, detail="Google ID not found in user session.")

        google_id = user["google_id"]

        # Establish MongoDB connection with invalid certificate allowance
        client = MongoClient(
            MONGO_URI,  # Replace with your actual MongoDB URI
            tls=True,
            tlsAllowInvalidCertificates=True
        )

        # Access database and collection
        db = client["mock_interview_platform"]  
        schedules_collection = db["schedules"]  

        # Query schedules by google_id
        schedules = schedules_collection.find_one({"user_google_id": google_id})
        if not schedules:
            raise HTTPException(status_code=404, detail="No schedule data found for this user.")

        print("Schedules retrieved successfully:", schedules)

        # Prepare response data
        profile_data = {
            "google_id": schedules.get("user_google_id"),
            "requests": schedules.get("requests", []),
            "scheduled_mocks": schedules.get("scheduled_mocks", []),
            "history": schedules.get("history", []),
        }

        client.close()

        return profile_data
    except Exception as e:
        logger.error(f"Error: {e}")
        return {"error": str(e)}

@router.get("/test-maindata")
async def test_get_match_data(google_id: str):
    'For testing purposes: test getting the data of the matches.'
    try:
        # Establish MongoDB connection with invalid certificate allowance
        client = MongoClient(
            MONGO_URI,  # Replace with your actual MongoDB URI
            tls=True,
            tlsAllowInvalidCertificates=True
        )

        # Access your database and collection
        db = client["mock_interview_platform"]
        schedules_collection = db["schedules"] 

        print("Connected to MongoDB")


        # Query schedules by google_id
        schedules = schedules_collection.find_one({"user_google_id": google_id})
        if not schedules:
            raise HTTPException(status_code=404, detail="No schedule data found for this user.")

        print("Schedules retrieved successfully:", schedules)

        # Prepare response data
        profile_data = {
            "google_id": schedules.get("user_google_id"),
            "requests": schedules.get("requests", []),
            "scheduled_mocks": schedules.get("scheduled_mocks", []),
            "history": schedules.get("history", []),
        }

        return profile_data
    except Exception as e:
        logger.error(f"Error: {e}")
        return {"error": str(e)}
