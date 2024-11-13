from mongoengine import connect, Document, StringField, DateTimeField, ListField, EmbeddedDocumentField, EmbeddedDocument, ObjectIdField
from datetime import datetime
from mongoengine import connection
from bson.objectid import ObjectId

# Connect to MongoDB
# connect(
#     host= in .env
# )

print(f"Connected to database: {connection.get_db().name}")

# Define the User model (embedded document)
from mongoengine import Document, StringField, DateTimeField, ListField, EmbeddedDocumentField, EmbeddedDocument
from datetime import datetime

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

# Query the schedules collection
schedules = Schedule.objects()

# Check if schedules exist and print each user's data
if schedules:
    print(f"Found {len(schedules)} schedule(s):")
    for schedule in schedules:
        print(f"User Google ID: {schedule.user_google_id}")
        
        print("Requests:")
        for request in schedule.requests:
            print(f"Request ID: {request._id}")
            print(f"Date: {request.date} | Time: {request.time} | Focus: {request.focus}")
            print(f"From: {request.from_user.name}, Profile Picture: {request.from_user.profile_picture}")
            print("----------------------------")

        print("Scheduled Mocks:")
        for mock in schedule.scheduled_mocks:
            print(f"Mock ID: {mock._id}")
            print(f"Date: {mock.date} | Time: {mock.time} | Focus: {mock.focus}")
            print(f"With: {mock.with_user.name}, Profile Picture: {mock.with_user.profile_picture}")
            print("----------------------------")

        print("History:")
        for history_item in schedule.history:
            print(f"History ID: {history_item._id}")
            print(f"Date: {history_item.date} | Time: {history_item.time} | Focus: {history_item.focus}")
            print(f"With: {history_item.with_user.name}, Profile Picture: {history_item.with_user.profile_picture}")
            print("----------------------------")
else:
    print("No schedules found in the database.")

print("Test complete.")
