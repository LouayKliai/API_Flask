# services/activity_service.py
from Models.activity_model import Activity  # Assuming you have the Activity model
from db import activity_collection  # Assuming you have the activity_collection

class ActivityService:
    @staticmethod
    def activity_exists_by_name(name):
        return activity_collection.find_one({'name': name}) is not None

    @staticmethod
    def create_activity(name, lesson_id, activity_type, activity_details):
        if ActivityService.activity_exists_by_name(name):
            raise ValueError('An activity with this name already exists.')

        activity_data = {
            'name': name,
            'lesson_id': lesson_id,
            'activity_type': activity_type,
            'activity_details': activity_details
        }
        activity_collection.insert_one(activity_data)

    @staticmethod
    def get_activities():
        # Add your logic to retrieve activities from the database
        # For example, you may use an ORM like SQLAlchemy or MongoDB driver
        activities = []  # Replace with actual retrieval logic
        return activities
