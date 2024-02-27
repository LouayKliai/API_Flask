from flask import Blueprint, jsonify, request
from Services.school_services import SchoolService  # Assuming you have a service for School

school_bp = Blueprint('school_bp', __name__)

@school_bp.route('/api/schools', methods=['POST'])
def add_school_route():
    school_data = request.json
    name = school_data.get('name')
    address = school_data.get('address')
    email = school_data.get('email')
    phone = school_data.get('phone')
    curriculum = school_data.get('curriculum', [])  # Default to an empty list if not provided

    try:
        new_school = SchoolService.create_school(name, address, email, phone, curriculum)
        return jsonify({'message': 'School added successfully', 'school': new_school.__dict__}), 201
    except ValueError as e:
        return jsonify({'message': str(e)}), 400

@school_bp.route('/api/schools', methods=['GET'])
def get_schools_route():
    # Implement logic to retrieve schools from the database
    schools = SchoolService.get_schools()  # Replace with actual retrieval logic
    return jsonify({'schools': schools})
