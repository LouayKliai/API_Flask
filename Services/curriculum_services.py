from Models.curriculum_model import Curriculum
from flask import jsonify
class CurriculumService:
    def create_curriculum(self, name,grades,subjects,owners):
        curriculum = Curriculum(name=name,grades=grades,subjects=subjects,owners=owners)  
        curriculum.save()  
        return str(curriculum.id)

    def get_curriculum(self, curriculum_id):
        curriculum = Curriculum.objects(id=curriculum_id).first()  
        return curriculum  
    

    def get_all_curriculum(self):
        return Curriculum.objects()
    

    def update_curriculum(self, curriculum_id, curriculum_data):
        curriculum = Curriculum.objects(id=curriculum_id).first()  
        if curriculum:
            curriculum.modify(**curriculum_data)  
            return True
        return False

    def delete_curriculum(self, curriculum_id):
        curriculum = Curriculum.objects(id=curriculum_id).first()  
        if curriculum:
            curriculum.delete()  
            return True
        return False

    def add_grade_to_curriculum(self, curriculum_id, grade):
        curriculum = Curriculum.objects(id=curriculum_id).first()  
        if curriculum:
            curriculum.grades.append(grade)  
            curriculum.save()  
            return True
        return False

    def remove_grade_from_curriculum(self, curriculum_id, grade_id):
        curriculum = Curriculum.objects(id=curriculum_id).first()  
        if curriculum:
            curriculum.grades.remove(grade_id)  
            curriculum.save()  
            return True
        return False

    def add_subject_to_curriculum(self, curriculum_id, subject):
        curriculum = Curriculum.objects(id=curriculum_id).first()  
        if curriculum:
            curriculum.subjects.append(subject)  
            curriculum.save()  
            return True
        return False
    def remove_subject_from_curriculum(self, curriculum_id, subject_id):
        curriculum = Curriculum.objects(id=curriculum_id).first() 
        if curriculum:
            if subject_id in curriculum.subjects:
                curriculum.subjects.remove(subject_id)  
                curriculum.save()  
                return True
        return False
