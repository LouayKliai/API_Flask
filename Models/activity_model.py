from mongoengine import Document, StringField, ReferenceField

class Activity(Document):
    name = StringField(required=True)
    lesson_id = ReferenceField('Lesson', required=True)
    activity_details = StringField()
