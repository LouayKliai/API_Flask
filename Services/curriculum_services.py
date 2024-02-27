# services/curriculum_service.py
from Models.curriculum_model import Curriculum  # Assuming you have the Curriculum model
from db import curriculum_collection  # Assuming you have the curriculum_collection

class CurriculumService:
    @staticmethod
    def curriculum_exists_by_name(name):
        return curriculum_collection.find_one({'name': name}) is not None

    @staticmethod
    def create_curriculum(name):
        if CurriculumService.curriculum_exists_by_name(name):
            raise ValueError('A curriculum with this name already exists.')

        curriculum_data = {
            'name': name,
            'grades': [],
            'subjects': []
        }
        curriculum_collection.insert_one(curriculum_data)
        return curriculum_data

    @staticmethod
    def get_curricula():
        # Add your logic to retrieve curricula from the database
        # For example, you may use an ORM like SQLAlchemy or MongoDB driver
        curricula = []  # Replace with actual retrieval logic
        return curricula
