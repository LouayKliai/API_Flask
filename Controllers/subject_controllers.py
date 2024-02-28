from flask import Blueprint, jsonify, request
from Services.subject_services import SubjectService

subject_bp = Blueprint('subject_bp', __name__)
subject_service = SubjectService()

@subject_bp.route('/subject', methods=['POST'])
def create_subject():
    data = request.json
    subject_id = subject_service.create_subject(data.get('name'), data.get('description'), data.get('topics'))
    return jsonify({"subject_id": str(subject_id)}), 201

@subject_bp.route('/subject/<subject_id>', methods=['GET'])
def get_subject(subject_id):
    subject = subject_service.get_subject(subject_id)
    if subject:
        return jsonify(subject), 200
    else:
        return jsonify({"message": "Subject not found"}), 404

@subject_bp.route('/subject/<subject_id>', methods=['PUT'])
def update_subject(subject_id):
    data = request.json
    updated_count = subject_service.update_subject(subject_id, data.get('name'), data.get('description'), data.get('topics'))
    if updated_count > 0:
        return jsonify({"message": "Subject updated successfully"}), 200
    else:
        return jsonify({"message": "Subject not found"}), 404

@subject_bp.route('/subject/<subject_id>', methods=['DELETE'])
def delete_subject(subject_id):
    deleted_count = subject_service.delete_subject(subject_id)
    if deleted_count > 0:
        return jsonify({"message": "Subject deleted successfully"}), 200
    else:
        return jsonify({"message": "Subject not found"}), 404
