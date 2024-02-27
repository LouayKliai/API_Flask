# services/resource_service.py
from Models.resource_model import Resource  # Assuming you have the Resource model
from db import resource_collection  # Assuming you have the resource_collection

class ResourceService:
    @staticmethod
    def resource_exists_by_type_name(type_name):
        return resource_collection.find_one({'type_name': type_name}) is not None

    @staticmethod
    def create_resource(type_name, description):
        if not type_name:
            raise ValueError('Resource type name is required for creating a resource.')

        if ResourceService.resource_exists_by_type_name(type_name):
            raise ValueError('A resource with this type name already exists.')

        new_resource = Resource(type_name, description)
        resource_collection.insert_one(new_resource.__dict__)
        return new_resource

    @staticmethod
    def get_resources():
        # Add your logic to retrieve resources from the database
        # For example, you may use an ORM like SQLAlchemy or MongoDB driver
        resources = []  # Replace with actual retrieval logic
        return resources
