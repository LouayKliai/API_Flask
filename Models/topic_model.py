from mongoengine import Document, StringField, ListField, ReferenceField
from Models.lesson_model import Lesson

class Topic(Document):
    name = StringField(required=True)
    description = StringField(required=True)
    lessons = ListField(ReferenceField(Lesson))
