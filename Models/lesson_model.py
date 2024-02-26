from flask import Flask
# from pymongo import MongoClient

class Lesson:
    def __init__(self, title, content, resources=[],question=[]):
        self.title = title
        self.content = content
        self.resources = resources
        self.question=question
        self.activities=[]

    # def save(self):
    #     client = MongoClient('mongodb://localhost:27017/')
    #     db = client['votre_base_de_donnees']
    #     lessons_collection = db['lessons']
    #     lesson_data = {
    #         "title": self.title,
    #         "content": self.content,
    #         "resources": self.resources
    #     }
    #     result = lessons_collection.insert_one(lesson_data)
    #     return result.inserted_id
