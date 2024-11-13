from mongoengine import connect, disconnect
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

def connect_db():
    """Connect to MongoDB"""
  # Ensure previous connections are closed
    connect(
        host = MONGO_URI
    )

def close_db():
    """Disconnect from MongoDB"""
    disconnect()  # Close the connection after each use
