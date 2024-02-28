# services/grade_service.py
from Models.grade_model import Grade  
from Models.curriculum_model import Curriculum 
from db import grade_collection 
from Services.curriculum_services import CurriculumService
class GradeService:
    def create_grade(self, name, curriculum_id):
        grade = Grade(name, curriculum_id)
        result = grade_collection.insert_one(grade.__dict__)
        return result.inserted_id

    def get_grade(self, grade_id):
        grade = grade_collection.find_one({"_id": grade_id})
        return grade

    def update_grade(self, grade_id, name):
        result = grade_collection.update_one({"_id": grade_id}, {"$set": {"name": name}})
        return result.modified_count

    def delete_grade(self, grade_id):
        result = grade_collection.delete_one({"_id": grade_id})
        return result.deleted_count