from Models.school_model import School  
from db import school_collection  

class SchoolService:
    def create_school(self, name, address, email, phone, curriculum=None):
        school = School(name, address, email, phone, curriculum)
        result = school_collection.insert_one(school.__dict__)
        return result.inserted_id

    def get_school(self, school_id):
        school = school_collection.find_one({"_id": school_id})
        return school

    def update_school(self, school_id, name=None, address=None, email=None, phone=None, curriculum=None):
        update_data = {}
        if name is not None:
            update_data["name"] = name
        if address is not None:
            update_data["address"] = address
        if email is not None:
            update_data["email"] = email
        if phone is not None:
            update_data["phone"] = phone
        if curriculum is not None:
            update_data["curriculum"] = curriculum
        
        result = school_collection.update_one({"_id": school_id}, {"$set": update_data})
        return result.modified_count

    def delete_school(self, school_id):
        result = school_collection.delete_one({"_id": school_id})
        return result.deleted_count