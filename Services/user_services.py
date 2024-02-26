from Models.user_model import User
from db import user_collection

class UserService:
    @staticmethod
    def user_exists_by_email(email):
        return user_collection.find_one({'email': email}) is not None

    @staticmethod
    def create_user(firstname, lastname, age, cin, email, password):
        user_data = {
            'firstname': firstname,
            'lastname': lastname,
            'age': age,
            'cin': cin,
            'email': email,
            'password': password
        }
        user_collection.insert_one(user_data)

    @staticmethod
    def login_user(email, password):
        user = user_collection.find_one({'email': email})
        if user is None:
            return None
        if user['password'] == password:
            return User(**user)
        return None
