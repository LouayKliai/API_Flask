from Models.school_model import School
class SchoolService:
    def create_school(self, name, address, email, phone, curriculum,user):
        school = School(name=name, address=address, email=email, phone=phone, curriculum=curriculum,user=user)
        school.save()
        return str(school.id)

    def get_school(self, school_id):
        school = School.objects(id=school_id).first()
        return school.to_json() if school else None

    def update_school(self, school_id, data):
        school = School.objects(id=school_id).first()
        if school:
            school.modify(**data)
            return True
        return False

    def delete_school(self, school_id):
        school = School.objects(id=school_id).first()
        if school:
            school.delete()
            return True
        return False
