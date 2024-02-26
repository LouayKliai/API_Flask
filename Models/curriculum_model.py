from flask import Flask

class Curriculum:
    def __init__(self, name):
        self.name = name
        self.grades = []
        self.subjects=[]