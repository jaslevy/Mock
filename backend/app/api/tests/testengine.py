from mongoengine import connect, Document, StringField, EmailField, DateTimeField, ListField, FloatField, IntField
from datetime import datetime
from mongoengine import connection

# Connect to MongoDB
# connect(
#     host= IN .ENV
# )

# Check the connected database name
print(f"Connected to database: {connection.get_db().name}")

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

# Check if users exist and print each user's data
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

print("Test complete.")

# # test_mongoengine.py

# from mongoengine import connect, Document, StringField, EmailField, DateTimeField, ListField, FloatField, IntField
# from datetime import datetime

# # 1. Define a User model using MongoEngine
# class User(Document):
#     google_id = StringField(required=True)
#     username = StringField(required=True)
#     first_name = StringField(required=True)
#     last_name = StringField(required=True)
#     email = EmailField(required=True)
#     bio = StringField(required=True)
#     bio_embedding = ListField(FloatField(), required=True)
#     profile_image = StringField(required=True)
#     interests = ListField(StringField(), required=True)
#     availability = IntField(required=True)
#     number_of_mocks = IntField(required=True)
#     created_at = DateTimeField(default=datetime.now, required=True)
#     education = ListField(StringField(), required=True)
#     experience = ListField(StringField(), required=True)

# # 2. Connect to MongoDB Atlas (use your own connection string here)
# connect(host="mongodb+srv://jl4537:mongo123@mockcluster.skhaw.mongodb.net/?retryWrites=true&w=majority&tlsAllowInvalidCertificates=true")

# # 3. Create a new user document
# new_user = User(
#     google_id="115257299020021775922",
#     username="jl4537",
#     first_name="Jasper",
#     last_name="Levy",
#     email="jl4537@cornell.edu",
#     bio="Software developer and tech enthusiast.",
#     bio_embedding=[0.1, 0.2, 0.3],
#     profile_image="path_to_profile_picture",
#     interests=["AI Search", "Full-Stack Dev", "RAG"],
#     availability=5,
#     number_of_mocks=3,
#     education=["Princeton", "Cornell Tech"],
#     experience=["Neo4j", "HP"]
# )

# # Save the user to the database
# new_user.save()

# # 4. Query all users from the database
# users = User.objects()

# # 5. Print each user to verify
# print(f"Found {len(users)} user(s):")
# for user in users:
#     print(f"User: {user.username} | Email: {user.email}")

# print("Test complete.")
