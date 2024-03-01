from Models.resource_model import Resource

class ResourceService:
    def create_resource(self, type_name, description):
        resource = Resource(type_name=type_name, description=description)
        resource.save()
        return str(resource.id)

    def get_resource(self, resource_id):
        resource = Resource.objects(id=resource_id).first()
        return resource.to_json() if resource else None

    def update_resource(self, resource_id, data):
        resource = Resource.objects(id=resource_id).first()
        if resource:
            resource.modify(**data)
            return True
        return False

    def delete_resource(self, resource_id):
        resource = Resource.objects(id=resource_id).first()
        if resource:
            resource.delete()
            return True
        return False
