# models/user.py

from pymongo import MongoClient
from bcrypt import hashpw, checkpw, gensalt

# MongoDB client setup
client = MongoClient("mongodb://localhost:27017/")
db = client['dark_web_monitoring']

class User:
    def __init__(self, email, password):
        self.email = email
        self.password = hashpw(password.encode('utf-8'), gensalt())

    def save(self):
        """Saves the user to the database."""
        db.users.insert_one({"email": self.email, "password": self.password})

    @staticmethod
    def find_by_email(email):
        """Finds a user by their email address."""
        return db.users.find_one({"email": email})

    @staticmethod
    def verify_password(plain_password, hashed_password):
        """Verifies if the provided password matches the hashed password."""
        return checkpw(plain_password.encode('utf-8'), hashed_password)
