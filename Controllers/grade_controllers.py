from flask import Blueprint, jsonify, request
from Services.grade_services import GradeService  # Assuming you have a service for Grade
from decrators import login_required

grade_bp = Blueprint('grade_bp', __name__)
grade_service = GradeService()

@grade_bp.route('/grade', methods=['POST'])
#@login_required
def create_grade():
    data = request.json
    grade_id = grade_service.create_grade(data.get('name'), data.get('curriculum'),data.get('document'))
    return jsonify({"grade_id": str(grade_id)}), 201

@grade_bp.route('/grade/<grade_id>', methods=['GET'])
#@login_required
def get_grade(grade_id):
    grade = grade_service.get_grade(grade_id)
    if grade:
        return jsonify(grade), 200
    else:
        return jsonify({"message": "Grade not found"}), 404


@grade_bp.route('/grade/<grade_id>', methods=['PUT'])
#@login_required
def update_grade(grade_id):
    data = request.json
    updated_count = grade_service.update_grade(grade_id, data.get('name'))
    if updated_count > 0:
        return jsonify({"message": "Grade updated successfully"}), 200
    else:
        return jsonify({"message": "Grade not found"}), 404


@grade_bp.route('/grade/<grade_id>', methods=['DELETE'])
#@login_required
def delete_grade(grade_id):
    deleted_count = grade_service.delete_grade(grade_id)
    if deleted_count > 0:
        return jsonify({"message": "Grade deleted successfully"}), 200
    else:
        return jsonify({"message": "Grade not found"}), 404