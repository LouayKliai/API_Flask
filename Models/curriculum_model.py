from mongoengine import Document, StringField, ReferenceField,ListField

class Curriculum(Document):
    name = StringField(required=True)
    grades = ListField(ReferenceField('Grade'))
    subjects = ListField(ReferenceField('Subject'))
