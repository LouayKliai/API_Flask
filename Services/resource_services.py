from Models.resource_model import Resource  
from db import ressource_collection  

class ResourceService:
    def create_resource(self, type_name, description):
        resource = Resource(type_name, description)
        result = ressource_collection.insert_one(resource.__dict__)
        return result.inserted_id

    def get_resource(self, resource_id):
        resource = ressource_collection.find_one({"_id": resource_id})
        return resource

    def update_resource(self, resource_id, type_name=None, description=None):
        update_data = {}
        if type_name is not None:
            update_data["type_name"] = type_name
        if description is not None:
            update_data["description"] = description
        
        result = ressource_collection.update_one({"_id": resource_id}, {"$set": update_data})
        return result.modified_count

    def delete_resource(self, resource_id):
        result = ressource_collection.delete_one({"_id": resource_id})
        return result.deleted_count