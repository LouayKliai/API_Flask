from mongoengine import Document, StringField, ListField, ReferenceField
from Models.activity_model import Activity
from Models.resource_model import Resource
from Models.question_model import  Question

class Lesson(Document):
    title = StringField(required=True)
    content = StringField(required=True)
    resources_list = ListField(ReferenceField(Resource))
    question_list = ListField(ReferenceField(Question))
    activities_list = ListField(ReferenceField(Activity))
