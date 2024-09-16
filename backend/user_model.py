from pymongo import MongoClient
from datetime import datetime

# Step 1: Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')  # Replace with your MongoDB URI if needed
db = client['mock_interview_platform']  # Database name
users_collection = db['users']  # Collection name

# Example user document
user = {
    "username": "john_doe",
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com",
    "bio": "Software engineer passionate about AI and machine learning.",
    "bio_embedding": [0.23, 0.56, 0.89, ...],  # Example vector embedding for the bio
    "profile_image": "https://s3.amazonaws.com/yourbucket/profile_image.jpg",
    "interests": ["Machine Learning", "Blockchain", "Startups"],
    "availability": 1,  # 0: Not Available, 1: Available, 2: Conditional Availability
    "interview_schedule": [datetime(2024, 9, 15, 14, 30), datetime(2024, 9, 16, 10, 0)],  # List of scheduled DateTime objects
    "friends": [],  # List of friend user IDs (MongoDB ObjectIds)
    "number_of_mocks": 0,  # Counter for the number of completed interviews
    "created_at": datetime.now()
}

# Step 2: Insert the document into MongoDB
result = users_collection.insert_one(user)
print(f"User inserted with ID: {result.inserted_id}")

# Step 3: Query to update the number of mocks for a user after an interview
user_id = result.inserted_id
users_collection.update_one(
    {"_id": user_id},
    {"$inc": {"number_of_mocks": 1}}  # Increment the number of completed mocks by 1
)

# Step 4: Add a friend by user ID
friend_id = ...  # Assume you have the friend's ObjectId
users_collection.update_one(
    {"_id": user_id},
    {"$push": {"friends": friend_id}}  # Add the friend's user ID to the list of friends
)

# Step 5: Query to retrieve the user and print their details
user_from_db = users_collection.find_one({"username": "john_doe"})
print(user_from_db)
