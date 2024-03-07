from mongoengine import Document, StringField, ReferenceField,ListField
from Models.subject_model import Subject
from Models.grade_model import Grade

class Curriculum(Document):
    name = StringField(required=True)
    grades = ListField(ReferenceField(Grade))
    subjects = ListField(ReferenceField(Subject))
