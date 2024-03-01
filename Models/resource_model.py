from flask import Flask
from mongoengine import Document, StringField

class Resource(Document):
    type_name = StringField(required=True)
    description = StringField(required=True)