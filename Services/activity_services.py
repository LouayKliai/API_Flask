from Models.activity_model import Activity
from db import activity_collection  

class ActivityService:
    def create_activity(self, activity_data):
        activity = Activity(**activity_data)
        result = activity_collection.insert_one(activity.__dict__)
        return result.inserted_id

    def get_activity(self, activity_id):
        activity = activity_collection.find_one({"_id": activity_id})
        return activity

    def update_activity(self, activity_id, activity_data):
        result = activity_collection.update_one({"_id": activity_id}, {"$set": activity_data})
        return result.modified_count

    def delete_activity(self, activity_id):
        result = activity_collection.delete_one({"_id": activity_id})
        return result.deleted_count