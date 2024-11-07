# backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.users import router as users_router
from app.api.auth import router as auth_router
from app.api.profile import router as profile_router  # Import the profile router
from app.db.database import connect_db, close_db


# # AUTH IMPORTS
from webbrowser import get
from fastapi import Depends, Request, HTTPException
from fastapi.responses import RedirectResponse
from authlib.integrations.starlette_client import OAuth
from starlette.middleware.sessions import SessionMiddleware
from app.api.oauth import google_oauth
from dotenv import load_dotenv
import os
from authlib.integrations.httpx_client import AsyncOAuth2Client 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "localhost:3000", "http://127.0.0.1:8000", "http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(profile_router, prefix="/api", tags=["Profile"])  # Include profile route

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

@app.on_event("startup")
def startup_db():
    connect_db()

@app.on_event("shutdown")
def shutdown_db():
    close_db()



# TEMPORARY: ADDING THE AUTH STUFF 

# Load environment variables
load_dotenv()
# Secret key for session management (storing session information in cookies)
app.add_middleware(
    SessionMiddleware,
    secret_key=os.environ.get('SESSION_SECRET', 'supersecret'),
    https_only=False,  # Use False for local development, True for production with HTTPS
    same_site="Lax"  # This ensures that the session cookie works properly across redirects

)
# Set up Google OAuth using the configuration in `app/oauth.py`
oauth = google_oauth()

@app.get("/")
async def read_root():
    return {"message": "Welcome to Google OAuth example"}
@app.get("/login")
async def login(request: Request):
    # Redirect to Google's OAuth page for login
    redirect_uri = "http://127.0.0.1:8000/auth/callback"

    return await oauth.google.authorize_redirect(request, redirect_uri)
# Geting the currnet user, if not logged in-> go to login
def get_current_user(request: Request):
    user = request.session.get("user")
    if not user:
        # Raise a 401 Unauthorized exception if the user is not authenticated
        raise HTTPException(status_code=401, detail="Not authenticated")
    return user
@app.get("/auth/callback")
async def auth_callback(request: Request):
    try:
        print("enter callback")
        token = await oauth.google.authorize_access_token(request)
        print("token recieved from google")
        
        id_token = token.get('id_token')
        if id_token is None:
            raise ValueError("No ID token found in the OAuth token response.")       
        user = token.get('userinfo')
        request.session['user'] = dict(user)
        return RedirectResponse(url='/profile')
    except Exception as e:
        print(f"Error during OAuth callback: {e}")
        return {"error": "OAuth callback failed"}
    
@app.get("/profile")
async def profile(request: Request, user: dict = Depends(get_current_user)):
    return {
        "message": f"Welcome to your dashboard, {user['email']}",
        # "user_data": user
    }   
@app.get('auth/logout')
async def logout(request: Request):
    request.session.pop('user', None)
    request.session.clear()
    return RedirectResponse(url='/')