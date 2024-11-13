# backend/app/api/profile.py
import json
from fastapi import APIRouter, HTTPException, Response
from fastapi.requests import Request
from pathlib import Path
import os
from app.models.schedules_model import Schedule
from app.models.user_model import User  # Assuming you have a User model
from datetime import datetime

import logging

logger = logging.getLogger(__name__)


router = APIRouter()

DEFAULT_GOOGLE_ID = "123456789012345678901"

@router.get("/maindata")
async def get_match_data(request: Request):
    try:
        # Get the google_id from the query parameter, or use the default if not provided
        google_id = request.query_params.get("google_id", DEFAULT_GOOGLE_ID)

        # Query the schedules collection and filter by user_google_id
        schedules = Schedule.objects(user_google_id=google_id)

        # Prepare the data to return in the same structure as match_profile_data.json
        profile_data = [
            {
                "google_id": schedule.user_google_id,
                "requests": [
                    {
                        "_id": request._id,
                        "date": request.date,
                        "time": request.time,
                        "focus": request.focus,
                        "from_user": {
                            "google_id": request.from_user.google_id,
                            "name": request.from_user.name,
                            "profile_picture": request.from_user.profile_picture
                        }
                    }
                    for request in schedule.requests
                ],
                "scheduled_mocks": [
                    {
                        "_id": mock._id,
                        "date": mock.date,
                        "time": mock.time,
                        "focus": mock.focus,
                        "with_user": {
                            "google_id": mock.with_user.google_id,
                            "name": mock.with_user.name,
                            "profile_picture": mock.with_user.profile_picture
                        }
                    }
                    for mock in schedule.scheduled_mocks
                ],
                "history": [
                    {
                        "_id": history_item._id,
                        "date": history_item.date,
                        "time": history_item.time,
                        "focus": history_item.focus,
                        "with_user": {
                            "google_id": history_item.with_user.google_id,
                            "name": history_item.with_user.name,
                            "profile_picture": history_item.with_user.profile_picture
                        }
                    }
                    for history_item in schedule.history
                ]
            }
            for schedule in schedules
        ]

        return profile_data
    except Exception as e:
        logger.error(f"Error: {e}")
        return {"error": str(e)}

 