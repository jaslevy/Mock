# models/user_model.py
from mongoengine import Document, StringField, EmailField, DateTimeField, ListField, EmbeddedDocumentField, EmbeddedDocument, ObjectIdField, FloatField, IntField
from datetime import datetime

# Define the User model
class User(Document):
    username = StringField(required=True)
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    email = EmailField(required=True)
    bio = StringField(required=True)
    bio_embedding = ListField(FloatField(required=True))
    profile_image = StringField(required=True)
    interests = ListField(StringField(required=True))
    availability = IntField(required=True)
    interview_schedule = ListField(DateTimeField(required=True))
    friends = ListField(ObjectIdField(required=True))
    number_of_mocks = IntField(required=True)
    created_at = DateTimeField(required=True, default=datetime.now)