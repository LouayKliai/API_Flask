from mongoengine import Document, StringField, ReferenceField,ListField
#from Models.curriculum_model import Curriculum

class Grade(Document):
    name = StringField(required=True)
    curriculum = ReferenceField("Curriculum")
    document=ListField(ReferenceField("Document"))
