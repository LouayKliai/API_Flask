from flask import Flask

class Resource:
    def __init__(self, type_name,description):
        self.type_name = type_name
        self.description=description
