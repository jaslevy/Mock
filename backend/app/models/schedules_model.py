from mongoengine import Document, StringField, ObjectIdField, DateTimeField, ListField, EmbeddedDocumentField, EmbeddedDocument
from datetime import datetime
from bson import ObjectId

class User(EmbeddedDocument):
    google_id = StringField(required=True)
    name = StringField(required=True)
    profile_picture = StringField(required=True)

class Request(EmbeddedDocument):
    _id = StringField(required=True)
    date = DateTimeField(required=True)
    time = StringField(required=True)
    focus = StringField(required=True)
    from_user = EmbeddedDocumentField(User, required=True)

class ScheduledMock(EmbeddedDocument):
    _id = StringField(required=True)
    date = DateTimeField(required=True)
    time = StringField(required=True)
    focus = StringField(required=True)
    with_user = EmbeddedDocumentField(User, required=True)

class History(EmbeddedDocument):
    _id = StringField(required=True)
    date = DateTimeField(required=True)
    time = StringField(required=True)
    focus = StringField(required=True)
    with_user = EmbeddedDocumentField(User, required=True)

class Schedule(Document):
    meta = {'collection': 'schedules'}  # Specify the collection name
    user_google_id = StringField(required=True)
    requests = ListField(EmbeddedDocumentField(Request))
    scheduled_mocks = ListField(EmbeddedDocumentField(ScheduledMock))
    history = ListField(EmbeddedDocumentField(History))