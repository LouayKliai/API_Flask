from flask import Blueprint, jsonify, request
from Services.activity_services import ActivityService  # Assuming you have a service for Activity

activity_bp = Blueprint('activity_bp', __name__)
activity_service = ActivityService()

@activity_bp.route('/activity', methods=['POST'])
def create_activity():
    data = request.get_json()
    lesson_id = data.get('lesson_id')   
    activity_id = activity_service.create_activity(lesson_id, data)
    return jsonify({'activity_id': str(activity_id)}), 201
@activity_bp.route('/activity/<activity_id>', methods=['GET'])
def get_activity(activity_id):
    activity = activity_service.get_activity(activity_id)
    if activity:
        return jsonify(activity), 200
    else:
        return jsonify({"message": "Activity not found"}), 404

@activity_bp.route('/activity/<activity_id>', methods=['PUT'])
def update_activity(activity_id):
    activity_data = request.json
    updated_count = activity_service.update_activity(activity_id, activity_data)
    if updated_count > 0:
        return jsonify({"message": "Activity updated successfully"}), 200
    else:
        return jsonify({"message": "Activity not found"}), 404

@activity_bp.route('/activity/<activity_id>', methods=['DELETE'])
def delete_activity(activity_id):
    deleted_count = activity_service.delete_activity(activity_id)
    if deleted_count > 0:
        return jsonify({"message": "Activity deleted successfully"}), 200
    else:
        return jsonify({"message": "Activity not found"}), 404