from flask import Flask
class User:
    def __init__(self, firstname, lastname, age,cin,email,password):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.cin=cin
        self.email = email
        self.password=password
    def to_dict(self):
        return {
            'firstname':self.firstname ,
            'lastname':self.lastname,
            'age':self.age ,
            'cin':self.cin,
            'email':self.email , 
            'password':self.password            
        }