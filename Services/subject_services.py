# services/subject_service.py
from Models.subject_model import Subject  # Assuming you have the Subject model
from db import subjects_collection  # Assuming you have the subjects_collection

class SubjectService:
    @staticmethod
    def subject_exists_by_name(name):
        return subjects_collection.find_one({'name': name}) is not None

    @staticmethod
    def create_subject(name, description, topics=[]):
        if not name:
            raise ValueError('Subject name is required for creating a subject.')

        if SubjectService.subject_exists_by_name(name):
            raise ValueError('A subject with this name already exists.')

        new_subject = Subject(name, description, topics)
        subjects_collection.insert_one(new_subject.__dict__)
        return new_subject

    @staticmethod
    def get_subjects():
        # Add your logic to retrieve subjects from the database
        # For example, you may use an ORM like SQLAlchemy or MongoDB driver
        subjects = []  # Replace with actual retrieval logic
        return subjects
