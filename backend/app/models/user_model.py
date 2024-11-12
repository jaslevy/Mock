# models/user_model.py
from mongoengine import Document, StringField, EmailField, DateTimeField, ListField, EmbeddedDocumentField, EmbeddedDocument, ObjectIdField, FloatField, IntField
from datetime import datetime
from bson import ObjectId


class User(Document):
    _id = ObjectIdField(primary_key=True, default=ObjectId)
    google_id = StringField(required=True)
    username = StringField(required=True)
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    email = EmailField(required=True)
    bio = StringField(required=True)
    bio_embedding = ListField(FloatField(required=True))
    profile_image = StringField(required=True)
    interests = ListField(StringField(required=True))
    availability = IntField(required=True)
    friends = ListField(ObjectIdField(required=True))
    number_of_mocks = IntField(required=True)
    created_at = DateTimeField(required=True, default=datetime.now)
    education = ListField(StringField(required=True))
    experience = ListField(StringField(required=True))