from mongoengine import Document, StringField, ListField, ReferenceField

class User(Document):
    google_id = StringField(required=True, unique=True)  # Unique Google ID
    email = StringField(required=True)
    first_name = StringField()
    last_name = StringField()
    bio = StringField(default="This is my bio.")  # Default bio
    profile_picture = StringField()
    schedules = ListField(ReferenceField('Schedule'))  # Placeholder for schedules
    friends = ListField(ReferenceField('User'))  # Placeholder for friends list
