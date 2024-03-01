from mongoengine import Document, StringField, ReferenceField
from Models.curriculum_model import Curriculum

class Grade(Document):
    name = StringField(required=True)
    curriculum = ReferenceField(Curriculum)
