from flask import Flask

class Curriculum:
    def __init__(self, name):
        self.name = name
        self.grades = []
        self.subjects=[]
    def add_grade(self, grade):
        self.grades.append(grade)

    def add_subject(self, subject):
        self.subjects.append(subject)