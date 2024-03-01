from mongoengine import Document, StringField, IntField

class User(Document):
    firstname = StringField(required=True)
    lastname = StringField(required=True)
    age = IntField(required=True)
    cin = StringField(required=True)
    email = StringField(required=True)
    password = StringField(required=True)
