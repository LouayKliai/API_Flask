from Models.grade_model import Grade

class GradeService:
    def create_grade(self, name, curriculum):
        grade = Grade(name=name, curriculum=curriculum)
        grade.save()
        return str(grade.id)

    def get_grade(self, grade_id):
        grade = Grade.objects(id=grade_id).first()
        return grade.to_json() if grade else None

    def update_grade(self, grade_id, data):
        grade = Grade.objects(id=grade_id).first()
        if grade:
            grade.modify(**data)
            return True
        return False

    def delete_grade(self, grade_id):
        grade = Grade.objects(id=grade_id).first()
        if grade:
            grade.delete()
            return True
        return False
