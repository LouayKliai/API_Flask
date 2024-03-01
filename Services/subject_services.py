from Models.subject_model import Subject

class SubjectService:
    def create_subject(self, name, description):
        subject = Subject(name=name, description=description)
        subject.save()
        return str(subject.id)

    def get_subject(self, subject_id):
        subject = Subject.objects(id=subject_id).first()
        return subject.to_json() if subject else None

    def update_subject(self, subject_id, data):
        subject = Subject.objects(id=subject_id).first()
        if subject:
            subject.modify(**data)
            return True
        return False

    def delete_subject(self, subject_id):
        subject = Subject.objects(id=subject_id).first()
        if subject:
            subject.delete()
            return True
        return False
