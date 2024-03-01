from mongoengine import Document, StringField, ListField, ReferenceField
from Models.topic_model import Topic

class Subject(Document):
    name = StringField(required=True)
    description = StringField(required=True)
    topics = ListField(ReferenceField(Topic))
