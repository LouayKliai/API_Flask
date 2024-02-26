from flask import Flask
# from pymongo import MongoClient

class Subject:
    def __init__(self, name, description, topics=[]):
        self.name = name
        self.description = description
        self.topics = topics

    # def save(self):
    #     client = MongoClient('mongodb://localhost:27017/')
    #     db = client['votre_base_de_donnees']
    #     subjects_collection = db['subjects']
    #     subject_data = {
    #         "name": self.name,
    #         "description": self.description,
    #         "topics": self.topics
    #     }
    #     result = subjects_collection.insert_one(subject_data)
    #     return result.inserted_id
