from mongoengine import Document, ReferenceField, ListField, DateTimeField, StringField
from datetime import datetime,timezone

class Project(Document):
    user_id = ReferenceField('User', required=True)
    curriculum_id = ReferenceField('Curriculum', required=True)
    edge = ListField(StringField())
    node = ListField(StringField())
    updated_at = DateTimeField(default=datetime.now(timezone.utc))
    created_at = DateTimeField(default=datetime.now(timezone.utc))