from mongoengine import Document, StringField, ReferenceField,ListField
from Models.subject_model import Subject
from Models.grade_model import Grade
from Models.user_model import User

class Curriculum(Document):
    name = StringField(required=True)
    grades = ListField(ReferenceField(Grade))
    subjects = ListField(ReferenceField(Subject))
    owners=ListField(ReferenceField(User))

    def to_dict(self):
            """
            Convertit l'objet Curriculum en un dictionnaire.
            """
            curriculum_dict = {
                'id': str(self.id),
                'name': self.name,
                'grades': [str(grade.id) for grade in self.grades],  # Convertir les références en ID
                'subjects': [str(subject.id) for subject in self.subjects],  
                'owners': [str(owner.id) for owner in self.owners],  
            }
            return curriculum_dict