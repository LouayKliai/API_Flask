from flask import Blueprint, jsonify, request
from Services.curriculum_services import CurriculumService  # Assuming you have a service for Curriculum

curriculum_bp = Blueprint('curriculum_bp', __name__)

@curriculum_bp.route('/api/curricula', methods=['POST'])
def add_curriculum_route():
    curriculum_data = request.json
    name = curriculum_data.get('name')

    try:
        new_curriculum = CurriculumService.create_curriculum(name)
        return jsonify({'message': 'Curriculum added successfully', 'curriculum': new_curriculum.__dict__}), 201
    except ValueError as e:
        return jsonify({'message': str(e)}), 400

@curriculum_bp.route('/api/curricula', methods=['GET'])
def get_curricula_route():
    # Implement logic to retrieve curricula from the database
    curricula = CurriculumService.get_curricula()  # Replace with actual retrieval logic
    return jsonify({'curricula': curricula})
