from mongoengine import Document, StringField, ReferenceField,ListField

class Activity(Document):
    name = StringField(required=True)
    lessons_id =ListField( ReferenceField('Lesson', required=True))
    activity_details = StringField()
