from flask import Flask
from Models.curriculum_model import Curriculum
class Grade:
    def __init__(self, name,curriculum):
        self.name = name
        self.curriculum = curriculum
        
