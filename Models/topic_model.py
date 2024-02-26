from flask import Flask
from pymongo import MongoClient
class Topic:
    def __init__(self, name,description, lessons=[]):
        self.name = name
        self.description = description
        self.lessons = lessons



    def save(self):
        client = MongoClient('mongodb://localhost:27017/')
        db = client['votre_base_de_donnees']
        topics_collection = db['topics']
        topic_data = {
            "name": self.name,
            "description": self.description,
            "lessons": self.lessons
        }
        result = topics_collection.insert_one(topic_data)
        return result.inserted_id
