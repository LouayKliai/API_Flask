from flask import Blueprint, jsonify, request
from Services.activity_services import ActivityService  # Assuming you have a service for Activity

activity_bp = Blueprint('activity_bp', __name__)

@activity_bp.route('/api/activities', methods=['POST'])
def add_activity_route():
    activity_data = request.json
    name = activity_data.get('name')
    lesson_id = activity_data.get('lesson_id')
    activity_type = activity_data.get('activity_type')
    activity_details = activity_data.get('activity_details')

    try:
        new_activity = ActivityService.create_activity(name, lesson_id, activity_type, activity_details)
        return jsonify({'message': 'Activity added successfully', 'activity': new_activity.__dict__}), 201
    except ValueError as e:
        return jsonify({'message': str(e)}), 400

@activity_bp.route('/api/activities', methods=['GET'])
def get_activities_route():
    # Implement logic to retrieve activities from the database
    activities = ActivityService.get_activities()  # Replace with actual retrieval logic
    return jsonify({'activities': activities})
