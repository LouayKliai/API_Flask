from mongoengine import Document, StringField, ReferenceField,ListField
from Models.activity_model import Activity

class Document(Document):
    name = StringField(required=True)
    document_type =StringField(required=True)
    list_activity=ListField(ReferenceField(Activity))
    
