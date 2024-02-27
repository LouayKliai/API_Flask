from flask import Blueprint, jsonify, request
from Services.resource_services import ResourceService  # Assuming you have a service for Resource

resource_bp = Blueprint('resource_bp', __name__)

@resource_bp.route('/api/resources', methods=['POST'])
def add_resource_route():
    resource_data = request.json
    type_name = resource_data.get('type_name')
    description = resource_data.get('description')

    try:
        new_resource = ResourceService.create_resource(type_name, description)
        return jsonify({'message': 'Resource added successfully', 'resource': new_resource.__dict__}), 201
    except ValueError as e:
        return jsonify({'message': str(e)}), 400

@resource_bp.route('/api/resources', methods=['GET'])
def get_resources_route():
    # Implement logic to retrieve resources from the database
    resources = ResourceService.get_resources()  # Replace with actual retrieval logic
    return jsonify({'resources': resources})
