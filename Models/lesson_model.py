from mongoengine import Document, StringField, ListField, ReferenceField
from Models.activity_model import Activity
from Models.resource_model import Resource
from Models.question_model import  Question

class Lesson(Document):
    title = StringField(required=True)
    content = StringField(required=True)
    resources = ListField(ReferenceField(Resource))
    question = ListField(ReferenceField(Question))
    activities = ListField(ReferenceField(Activity))
