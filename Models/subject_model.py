from flask import Flask

class Subject:
    def __init__(self, name, description, topics=[]):
        self.name = name
        self.description = description
        self.topics = topics
