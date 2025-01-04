### Next steps:
# 1. Once this is figured out, logic for CRUD operations should be added (aside read obviously)
#  Long term: Ultimately, have this easily ported for other administrators (From other campuses) to set up with some technical 
#        knowledge of deployment and mongodb necessary. Include instructions for that.


# backend/app/main.py
from re import U
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.users import router as users_router
from app.api.auth import router as auth_router
from app.api.profile import router as profile_router  # Import the profile router

### AUTH IMPORTS
from webbrowser import get
from fastapi import Depends, Request, HTTPException
from fastapi.responses import RedirectResponse, JSONResponse
from authlib.integrations.starlette_client import OAuth
from starlette.middleware.sessions import SessionMiddleware
from app.api.oauth import google_oauth
from dotenv import load_dotenv
import os
from authlib.integrations.httpx_client import AsyncOAuth2Client 

### DB IMPORTS
from app.db.database import connect_db, close_db
from app.api.user_model import User

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongo.errors import ConnectionFailure 


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "localhost:3000", "http://127.0.0.1:8000", "http://localhost:8000", "http://192.168.1.238:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# NOTE: Question, do we need this? 
@app.on_event("startup")
async def startup_event():  
    connect_db()

@app.on_event("shutdown")
async def shutdown_event():
    pass
    close_db()


# NOTE: AUTH segment here 

app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(profile_router, prefix="/api", tags=["Profile"])  # Include profile route


# Load environment variables
load_dotenv()
# Secret key for session management (storing session information in cookies)
app.add_middleware(
    SessionMiddleware,
    secret_key=os.environ.get('SESSION_SECRET', 'supersecret'),
    https_only=False,  # Use False for local development, True for production with HTTPS
    same_site="none"  # This ensures that the session cookie works properly across redirects 
    # NOTE: For now we can only run on safari) (Chrome only allwos same_site=None for production (https))
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



MONGO_URI = os.getenv("MONGO_URI")
@app.get("/auth/callback")
async def auth_callback(request: Request):
    try:
        # Retrieve token from Google OAuth
        token = await oauth.google.authorize_access_token(request)
        userinfo = token.get('userinfo')
        if not userinfo:
            raise ValueError("User info not returned by Google")

        # Extract user data
        google_id = userinfo['sub']
        email = userinfo.get("email")
        first_name = userinfo.get("given_name", "")
        last_name = userinfo.get("family_name", "")
        profile_picture = userinfo.get("picture", "")

        # Initialize MongoDB client locally within the function
        client = MongoClient(MONGO_URI, tls=True, tlsAllowInvalidCertificates=True)
        db = client["mock_interview_platform"]  
        users_collection = db["users"] 
        schedules_collection = db["schedules"]  


        # Check if user exists in MongoDB
        user = users_collection.find_one({"google_id": google_id})

        if user:
            # Update user data
            users_collection.update_one(
                {"google_id": google_id},
                {"$set": {
                    "email": email,
                    "first_name": first_name,
                    "last_name": last_name,
                    "profile_picture": profile_picture
                }}
            )
        else:
            # Insert new user into MongoDB
            new_user = {
                "google_id": google_id,
                "email": email,
                "first_name": first_name,
                "last_name": last_name,
                "bio": "This is my bio.",  # Default bio
                "profile_picture": profile_picture,
                "schedules": [],  # Default schedules
                "friends": []  # Default friends list
            }
            users_collection.insert_one(new_user)

        # Check if a schedule exists for this user
        schedule = schedules_collection.find_one({"user_google_id": google_id})

        if not schedule:
            # Add a default schedule for the user
            new_schedule = {
                "user_google_id": google_id,
                "requests": [],  # Default requests
                "scheduled_mocks": [],  # Default scheduled mocks
                "history": []  # Default history
            }
            schedules_collection.insert_one(new_schedule)

        # Store minimal user info in the session
        request.session['user'] = {"google_id": google_id}

        # Close MongoDB connection
        client.close()

        # Redirect to profile page
        return RedirectResponse(url='http://localhost:3000/profile')
        
    except Exception as e:
        # Log and return the error
        print(f"Error during OAuth callback: {e}")
        return JSONResponse(
            status_code=400,
            content={"error": "OAuth callback failed", "details": str(e)}
        )
    
@app.get("/profile")
async def profile(request: Request, user: dict = Depends(get_current_user)):
    try:
        # Extract the Google ID from the session
        google_id = user["google_id"]

        # Query MongoDB for the user's full profile
        client = MongoClient(MONGO_URI, tls=True, tlsAllowInvalidCertificates=True)
        db = client["mock_interview_platform"]  # Replace with your actual database name
        users_collection = db["users"]  # Replace with your collection name

        user_data = users_collection.find_one({"google_id": google_id})

        if not user_data:
            return {
                "error": "User not found in the database",
                "google_id": google_id
            }

        # Remove MongoDB's ObjectId field from the response
        user_data.pop("_id", None)

        # Return enriched profile data
        return {
            "message": f"Welcome to your dashboard, {user_data['email']}",
            "profile": user_data
        }

    except Exception as e:
        print(f"Error retrieving profile: {e}")
        return {"error": "Failed to retrieve profile", "details": str(e)}


    
@app.get('auth/logout')
async def logout(request: Request):
    request.session.pop('user', None)
    request.session.clear()
    return RedirectResponse(url='/')


# DATABASE TEST: MONGOENGINE
@app.get("/test-db")
async def test_db():
    '''TESTING CODE: VALIDATING CONNECTION TO DATABASE'''

    client = MongoClient(MONGO_URI, tls=True, tlsAllowInvalidCertificates=True)

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)


@app.get("/inspect-db")
async def inspect_database():
    '''TESTING CODE: FOR INSPECTING DATABASE'''
    try:
        # Create MongoDB client with bypassing SSL validation
        client = MongoClient(MONGO_URI, tls=True, tlsAllowInvalidCertificates=True)

        # Get list of databases
        databases = client.list_database_names()

        # Example: Inspect the "my_database" database
        db = client["my_database"]  # Replace with your actual database name
        collections = db.list_collection_names()

        # Example: Preview documents in the "my_collection" collection
        collection = db["my_collection"]  # Replace with your collection name
        documents = list(collection.find().limit(5))  # Fetch up to 5 documents for preview

        # Return the inspection results
        return {
            "databases": databases,
            "collections": collections,
            "documents": documents,
        }

    except ConnectionFailure as e:
        return {"error": "Failed to connect to MongoDB", "details": str(e)}

    except Exception as e:
        return {"error": "An unexpected error occurred", "details": str(e)}
    
@app.get("/match-data")
async def match_data(request: Request, user: dict = Depends(get_current_user)):
    try:
        google_id = user["google_id"]
        client = MongoClient(MONGO_URI, tls=True, tlsAllowInvalidCertificates=True)
        db = client["mock_interview_platform"]
        users_collection = db["users"]

        # Fetch user data for the match interface
        user_data = users_collection.find_one({"google_id": google_id})
        if not user_data:
            return {"error": "User not found"}

        return {
            "google_id": google_id,
            "profile_picture": user_data.get("profile_picture"),
            "bio": user_data.get("bio"),
            "friends": user_data.get("friends"),
            "schedules": user_data.get("schedules"),
        }
    except Exception as e:
        print(f"Error retrieving match data: {e}")
        return {"error": "Failed to retrieve match data", "details": str(e)}


@app.get("/profile/edit")
async def edit_profile(request: Request, user: dict = Depends(get_current_user)):
    try:
        google_id = user["google_id"]


        # Fetch user data from MongoDB
        client = MongoClient(MONGO_URI, tls=True, tlsAllowInvalidCertificates=True)
        db = client["mock_interview_platform"]
        users_collection = db["users"]

        user_data = users_collection.find_one({"google_id": google_id}, {"_id": 0})
        if not user_data:
            return {"error": "User not found"}

        return {"profile": user_data}
    except Exception as e:
        print(f"Error fetching profile data: {e}")
        return {"error": "Failed to fetch profile data", "details": str(e)}

@app.put("/profile/edit")
async def update_profile(request: Request, user: dict = Depends(get_current_user)):
    try:
        google_id = user["google_id"]
        updated_data = await request.json()

        # Update user data in MongoDB
        client = MongoClient(MONGO_URI, tls=True, tlsAllowInvalidCertificates=True)
        db = client["mock_interview_platform"]
        users_collection = db["users"]

        users_collection.update_one(
            {"google_id": google_id},
            {"$set": updated_data}
        )

        return {"message": "Profile updated successfully"}
    except Exception as e:
        print(f"Error updating profile: {e}")
        return {"error": "Failed to update profile", "details": str(e)}
