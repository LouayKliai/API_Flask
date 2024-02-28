from Models.subject_model import Subject  
from db import subject_collection  

class SubjectService:
    def create_subject(self, name, description, topics=None):
        subject = Subject(name, description, topics)
        result = subject_collection.insert_one(subject.__dict__)
        return result.inserted_id

    def get_subject(self, subject_id):
        subject = subject_collection.find_one({"_id": subject_id})
        return subject

    def update_subject(self, subject_id, name=None, description=None, topics=None):
        update_data = {}
        if name is not None:
            update_data["name"] = name
        if description is not None:
            update_data["description"] = description
        if topics is not None:
            update_data["topics"] = topics
        
        result = subject_collection.update_one({"_id": subject_id}, {"$set": update_data})
        return result.modified_count

    def delete_subject(self, subject_id):
        result = subject_collection.delete_one({"_id": subject_id})
        return result.deleted_count
