from Models.curriculum_model import Curriculum 
from db import curriculum_collection  


class CurriculumService:
    def create_curriculum(self, name):
        curriculum = Curriculum(name)
        result = curriculum_collection.insert_one(curriculum.__dict__)
        return result.inserted_id

    def get_curriculum(self, curriculum_id):
        curriculum = curriculum_collection.find_one({"_id": curriculum_id})
        return curriculum

    def update_curriculum(self, curriculum_id, curriculum_data):
        result = curriculum_collection.update_one({"_id": curriculum_id}, {"$set": curriculum_data})
        return result.modified_count

    def delete_curriculum(self, curriculum_id):
        result = curriculum_collection.delete_one({"_id": curriculum_id})
        return result.deleted_count

    def add_grade_to_curriculum(self, curriculum_id, grade):
        curriculum = curriculum_collection.find_one({"_id": curriculum_id})
        if curriculum:
            curriculum['grades'].append(grade)
            curriculum_collection.update_one({"_id": curriculum_id}, {"$set": curriculum})
            return True
        return False
    def remove_grade_from_curriculum(self, curriculum_id, grade_id):
        result = curriculum_collection.update_one({"_id": curriculum_id}, {"$pull": {"grades": grade_id}})
        return result.modified_count

    def add_subject_to_curriculum(self, curriculum_id, subject):
        curriculum = curriculum_collection.find_one({"_id": curriculum_id})
        if curriculum:
            curriculum['subjects'].append(subject)
            curriculum_collection.update_one({"_id": curriculum_id}, {"$set": curriculum})
            return True
        return False
