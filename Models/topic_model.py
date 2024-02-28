from flask import Flask
class Topic:
    def __init__(self, name,description, lessons=[]):
        self.name = name
        self.description = description
        self.lessons = lessons