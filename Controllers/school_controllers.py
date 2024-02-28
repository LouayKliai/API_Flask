from flask import Blueprint, jsonify, request
from Services.school_services import SchoolService 

school_bp = Blueprint('school_bp', __name__)
school_service = SchoolService()

@school_bp.route('/school', methods=['POST'])
def create_school():
    data = request.json
    school_id = school_service.create_school(data.get('name'), data.get('address'), data.get('email'), data.get('phone'), data.get('curriculum'))
    return jsonify({"school_id": str(school_id)}), 201

@school_bp.route('/school/<school_id>', methods=['GET'])
def get_school(school_id):
    school = school_service.get_school(school_id)
    if school:
        return jsonify(school), 200
    else:
        return jsonify({"message": "School not found"}), 404

@school_bp.route('/school/<school_id>', methods=['PUT'])
def update_school(school_id):
    data = request.json
    updated_count = school_service.update_school(school_id, data.get('name'), data.get('address'), data.get('email'), data.get('phone'), data.get('curriculum'))
    if updated_count > 0:
        return jsonify({"message": "School updated successfully"}), 200
    else:
        return jsonify({"message": "School not found"}), 404

@school_bp.route('/school/<school_id>', methods=['DELETE'])
def delete_school(school_id):
    deleted_count = school_service.delete_school(school_id)
    if deleted_count > 0:
        return jsonify({"message": "School deleted successfully"}), 200
    else:
        return jsonify({"message": "School not found"}), 404
