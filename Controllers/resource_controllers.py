from flask import Blueprint, jsonify, request
from Services.resource_services import ResourceService 
from decrators import login_required

resource_bp = Blueprint('resource_bp', __name__)
resource_service = ResourceService()

@resource_bp.route('/resource', methods=['POST'])
#@login_required
def create_resource():
    data = request.json
    resource_id = resource_service.create_resource(data.get('type_name'), data.get('description'))
    return jsonify({"resource_id": str(resource_id)}), 201

@resource_bp.route('/resource/<resource_id>', methods=['GET'])
#@login_required
def get_resource(resource_id):
    resource = resource_service.get_resource(resource_id)
    if resource:
        return jsonify(resource), 200
    else:
        return jsonify({"message": "Resource not found"}), 404

@resource_bp.route('/resource/<resource_id>', methods=['PUT'])
#@login_required
def update_resource(resource_id):
    data = request.json
    updated_count = resource_service.update_resource(resource_id, data.get('type_name'), data.get('description'))
    if updated_count > 0:
        return jsonify({"message": "Resource updated successfully"}), 200
    else:
        return jsonify({"message": "Resource not found"}), 404

@resource_bp.route('/resource/<resource_id>', methods=['DELETE'])
#@login_required
def delete_resource(resource_id):
    deleted_count = resource_service.delete_resource(resource_id)
    if deleted_count > 0:
        return jsonify({"message": "Resource deleted successfully"}), 200
    else:
        return jsonify({"message": "Resource not found"}), 404