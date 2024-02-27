from flask import Blueprint, jsonify, request
from Services.subject_services import SubjectService  # Assuming you have a service for Subject

subject_bp = Blueprint('subject_bp', __name__)

@subject_bp.route('/api/subjects', methods=['POST'])
def add_subject_route():
    subject_data = request.json
    name = subject_data.get('name')
    description = subject_data.get('description')
    topics = subject_data.get('topics', [])  # Default to an empty list if not provided

    try:
        new_subject = SubjectService.create_subject(name, description, topics)
        return jsonify({'message': 'Subject added successfully', 'subject': new_subject.__dict__}), 201
    except ValueError as e:
        return jsonify({'message': str(e)}), 400

@subject_bp.route('/api/subjects', methods=['GET'])
def get_subjects_route():
    # Implement logic to retrieve subjects from the database
    subjects = SubjectService.get_subjects()  # Replace with actual retrieval logic
    return jsonify({'subjects': subjects})
