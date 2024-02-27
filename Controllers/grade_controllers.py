from flask import Blueprint, jsonify, request
from Services.grade_services import GradeService  # Assuming you have a service for Grade

grade_bp = Blueprint('grade_bp', __name__)

@grade_bp.route('/api/grades', methods=['POST'])
def add_grade_route():
    grade_data = request.json
    name = grade_data.get('name')
    curriculum_id = grade_data.get('curriculum_id')  # Assuming you pass curriculum_id instead of the full curriculum object

    try:
        new_grade = GradeService.create_grade(name, curriculum_id)
        return jsonify({'message': 'Grade added successfully', 'grade': new_grade.__dict__}), 201
    except ValueError as e:
        return jsonify({'message': str(e)}), 400

@grade_bp.route('/api/grades', methods=['GET'])
def get_grades_route():
    # Implement logic to retrieve grades from the database
    grades = GradeService.get_grades()  # Replace with actual retrieval logic
    return jsonify({'grades': grades})
