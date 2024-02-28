from Models.user_model import User
from db import user_collection

class UserService:
    def create_user(self, firstname, lastname, age, cin, email, password):
        user = User(firstname, lastname, age, cin, email, password)
        result = user_collection.insert_one(user.to_dict())
        return result.inserted_id

    def get_user(self, user_id):
        user = user_collection.find_one({"_id": user_id})
        return user

    def update_user(self, user_id, firstname=None, lastname=None, age=None, cin=None, email=None, password=None):
        update_data = {}
        if firstname is not None:
            update_data["firstname"] = firstname
        if lastname is not None:
            update_data["lastname"] = lastname
        if age is not None:
            update_data["age"] = age
        if cin is not None:
            update_data["cin"] = cin
        if email is not None:
            update_data["email"] = email
        if password is not None:
            update_data["password"] = password
        
        result = user_collection.update_one({"_id": user_id}, {"$set": update_data})
        return result.modified_count

    def delete_user(self, user_id):
        result = user_collection.delete_one({"_id": user_id})
        return result.deleted_count