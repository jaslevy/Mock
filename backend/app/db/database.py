from mongoengine import connect, disconnect
from dotenv import load_dotenv
import os
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")



MONGO_URI = "mongodb://localhost:27017"

def connect_db():
    connect(db="your_database_name", host=MONGO_URI)

def close_db():
    disconnect()