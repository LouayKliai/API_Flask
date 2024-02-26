from flask import Flask

class School:
    def __init__(self, name, address, email, phone,curriculum=[]):
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone
        self.curriculum=curriculum

# {
#     _id: ObjectId,
#     name: String,
#     location: String,
#     curriculums: [ObjectId] // Array of curriculum ObjectId references
# }