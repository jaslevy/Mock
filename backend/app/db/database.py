from mongoengine import connect, disconnect
from models.user_model import User

# Connect to the database
connect('mydatabase', host='mongodb://localhost:27017/')

def get_user(username: str) -> User:
    """Get a user from the database."""
    return User.objects.get(username=username)