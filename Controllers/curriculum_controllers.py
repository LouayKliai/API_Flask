from flask import Blueprint, jsonify, request
from Services.curriculum_services import CurriculumService  

curriculum_bp = Blueprint('curriculum_bp', __name__)
curriculum_service = CurriculumService()



@curriculum_bp.route('/curriculum', methods=['POST'])
def create_curriculum():
    data = request.get_json()
    name = data.get('name')
    if name:
        curriculum_id = curriculum_service.create_curriculum(name)
        return jsonify({'curriculum_id': str(curriculum_id)}), 201
    else:
        return jsonify({'error': 'Missing name parameter'}), 400

@curriculum_bp.route('/curriculum/<curriculum_id>', methods=['GET'])
def get_curriculum(curriculum_id):
    curriculum = curriculum_service.get_curriculum(curriculum_id)
    if curriculum:
        return jsonify(curriculum.to_dict()), 200
    else:
        return jsonify({'error': 'Curriculum not found'}), 404

@curriculum_bp.route('/curriculum/<curriculum_id>', methods=['PUT'])
def update_curriculum(curriculum_id):
    data = request.get_json()
    success = curriculum_service.update_curriculum(curriculum_id, data)
    if success:
        return jsonify({'message': 'Curriculum updated successfully'}), 200
    else:
        return jsonify({'error': 'Curriculum not found'}), 404

@curriculum_bp.route('/curriculum/<curriculum_id>', methods=['DELETE'])
def delete_curriculum(curriculum_id):
    success = curriculum_service.delete_curriculum(curriculum_id)
    if success:
        return jsonify({'message': 'Curriculum deleted successfully'}), 200
    else:
        return jsonify({'error': 'Curriculum not found'}), 404
