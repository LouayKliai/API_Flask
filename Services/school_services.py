# services/school_service.py
from Models.school_model import School  # Assuming you have the School model
from db import school_collection  # Assuming you have the school_collection

class SchoolService:
    @staticmethod
    def school_exists_by_name(name):
        return school_collection.find_one({'name': name}) is not None

    @staticmethod
    def create_school(name, address, email, phone, curriculum=[]):
        if not name:
            raise ValueError('School name is required for creating a school.')

        if SchoolService.school_exists_by_name(name):
            raise ValueError('A school with this name already exists.')

        new_school = School(name, address, email, phone, curriculum)
        school_collection.insert_one(new_school.__dict__)
        return new_school

    @staticmethod
    def get_schools():
        # Add your logic to retrieve schools from the database
        # For example, you may use an ORM like SQLAlchemy or MongoDB driver
        schools = []  # Replace with actual retrieval logic
        return schools
