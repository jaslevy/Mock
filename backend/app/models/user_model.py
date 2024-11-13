 # backend/app/models/user_model.py
from mongoengine import Document, StringField, EmailField, ListField, FloatField, IntField, DateTimeField
from datetime import datetime

class User(Document):
    meta = {'collection': 'users'}  # Specify the collection name

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

    # Optional: Add friends field if required
    friends = ListField(StringField(), required=False)  

