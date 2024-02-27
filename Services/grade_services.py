# services/grade_service.py
from Models.grade_model import Grade  
from Models.curriculum_model import Curriculum 
from db import grade_collection 
from Services.curriculum_services import CurriculumService
class GradeService:
    @staticmethod
    def grade_exists_by_name(name):
        return grade_collection.find_one({'name': name}) is not None

    @staticmethod
    def create_grade(name, curriculum_id):
        if not curriculum_id:
            raise ValueError('Curriculum ID is required for creating a grade.')

        if not CurriculumService.curriculum_exists_by_id(curriculum_id):
            raise ValueError('Curriculum with the provided ID does not exist.')

        if GradeService.grade_exists_by_name(name):
            raise ValueError('A grade with this name already exists.')

        new_grade = Grade(name, curriculum_id)
        grade_collection.insert_one(new_grade.__dict__)
        return new_grade

    @staticmethod
    def get_grades():
        # Add your logic to retrieve grades from the database
        # For example, you may use an ORM like SQLAlchemy or MongoDB driver
        grades = []  # Replace with actual retrieval logic
        return grades
