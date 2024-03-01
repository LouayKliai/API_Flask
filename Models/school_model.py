from flask import Flask
from mongoengine import Document,StringField,ListField,ReferenceField
from Models.curriculum_model import Curriculum
class School(Document):
    name = StringField(required=True)
    address = StringField(required=True)
    email = StringField(required=True)
    phone = StringField(required=True)
    curriculum = ListField(ReferenceField(Curriculum))