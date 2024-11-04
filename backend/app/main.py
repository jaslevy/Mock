# backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.users import router as users_router
from app.api.auth import router as auth_router
from app.api.profile import router as profile_router  # Import the profile router
from app.db.database import connect_db, close_db

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3001", "http://127.0.0.1:3001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(profile_router, prefix="/profile", tags=["Profile"])  # Include profile route

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

@app.on_event("startup")
def startup_db():
    connect_db()

@app.on_event("shutdown")
def shutdown_db():
    close_db()
