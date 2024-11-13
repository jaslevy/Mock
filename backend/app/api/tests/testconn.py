from mongoengine import connect, Document, StringField, EmailField, ListField, FloatField, IntField, DateTimeField
from datetime import datetime

import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")


# Connect to MongoDB
connect(
    host=MONGO_URI
)

# Define the User model
class User(Document):
    meta = {'collection': 'users'}
    google_id = StringField(required=True)
    username = StringField(required=True)
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    email = EmailField(required=True)
    bio = StringField(required=True)
    bio_embedding = ListField(FloatField(), required=True)
    profile_image = StringField(required=True)
    interests = ListField(StringField(), required=True)
    availability = IntField(required=True)
    number_of_mocks = IntField(required=True)
    created_at = DateTimeField(default=datetime.now, required=True)
    education = ListField(StringField(), required=True)
    experience = ListField(StringField(), required=True)
    
    # Add the friends field
    friends = ListField(StringField(), required=False)  

# Query all users
users = User.objects()

# Print each user's data
if users:
    print(f"Found {len(users)} user(s):")
    for user in users:
        print(f"User: {user.username} | Email: {user.email}")
        print(f"First Name: {user.first_name} | Last Name: {user.last_name}")
        print(f"Interests: {user.interests}")
        print(f"Education: {user.education}")
        print(f"Experience: {user.experience}")
        print(f"User ID: {user.id}")  # Accessing the _id field directly
        print("----------------------------")
else:
    print("No users found in the database.")
