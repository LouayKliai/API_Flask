from flask import Blueprint, jsonify, request
from Services.curriculum_services import CurriculumService  

curriculum_bp = Blueprint('curriculum_bp', __name__)
curriculum_service = CurriculumService()


@curriculum_bp.route('/curriculum', methods=['POST'])
def create_curriculum():
    data = request.json
    curriculum_id = curriculum_service.create_curriculum(data.get('name'))
    return jsonify({"curriculum_id": str(curriculum_id)}), 201

@curriculum_bp.route('/curriculum/<curriculum_id>', methods=['GET'])
def get_curriculum(curriculum_id):
    curriculum = curriculum_service.get_curriculum(curriculum_id)
    if curriculum:
        return jsonify(curriculum), 200
    else:
        return jsonify({"message": "Curriculum not found"}), 404

@curriculum_bp.route('/curriculum/<curriculum_id>', methods=['PUT'])
def update_curriculum(curriculum_id):
    data = request.json
    updated_count = curriculum_service.update_curriculum(curriculum_id, data)
    if updated_count > 0:
        return jsonify({"message": "Curriculum updated successfully"}), 200
    else:
        return jsonify({"message": "Curriculum not found"}), 404

@curriculum_bp.route('/curriculum/<curriculum_id>', methods=['DELETE'])
def delete_curriculum(curriculum_id):
    deleted_count = curriculum_service.delete_curriculum(curriculum_id)
    if deleted_count > 0:
        return jsonify({"message": "Curriculum deleted successfully"}), 200
    else:
        return jsonify({"message": "Curriculum not found"}), 404

@curriculum_bp.route('/curriculum/<curriculum_id>/grade', methods=['POST'])
def add_grade_to_curriculum(curriculum_id):
    data = request.json
    if curriculum_service.add_grade_to_curriculum(curriculum_id, data.get('grade')):
        return jsonify({"message": "Grade added to curriculum successfully"}), 200
    else:
        return jsonify({"message": "Curriculum not found"}), 404

@curriculum_bp.route('/curriculum/<curriculum_id>/grade/<grade_id>', methods=['DELETE'])
def remove_grade_from_curriculum(curriculum_id, grade_id):
    if curriculum_service.remove_grade_from_curriculum(curriculum_id, grade_id):
        return jsonify({"message": "Grade removed from curriculum successfully"}), 200
    else:
        return jsonify({"message": "Curriculum or grade not found"}), 404

@curriculum_bp.route('/curriculum/<curriculum_id>/subject', methods=['POST'])
def add_subject_to_curriculum(curriculum_id):
    data = request.json
    if curriculum_service.add_subject_to_curriculum(curriculum_id, data.get('subject')):
        return jsonify({"message": "Subject added to curriculum successfully"}), 200
    else:
        return jsonify({"message": "Curriculum not found"}), 404
