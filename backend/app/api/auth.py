# backend/app/api/auth.py
import json
from fastapi import APIRouter, HTTPException, Depends, status, Form
from pathlib import Path

router = APIRouter()

# Load admin data from admin_data.json
def load_admin_data():
    admin_data_path = Path(__file__).parent.parent / "admin_data.json"
    with open(admin_data_path, 'r') as f:
        return json.load(f)

@router.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    admin_data = load_admin_data()

    # Validate credentials
    if username == admin_data["username"] and password == admin_data["password"]:
        return {"status": "success", "message": "Logged in successfully"}

    # If credentials don't match, raise an error
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password"
    )
