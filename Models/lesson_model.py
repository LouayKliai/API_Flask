from flask import Flask
class Lesson:
    def __init__(self, title, content, resources=[],question=[]):
        self.title = title
        self.content = content
        self.resources = resources
        self.question=question
        self.activities=[]
