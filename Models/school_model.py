from flask import Flask
from mongoengine import Document,StringField
class School(Document):
    name = StringField(required=True)
    address = StringField(required=True)
    email = StringField(required=True)
    phone = StringField(required=True)
    curriculum = StringField()