from flask import Blueprint, jsonify, request
from Services.activity_services import ActivityService  # Assuming you have a service for Activity
from decrators import login_required
activity_bp = Blueprint('activity_bp', __name__)
activity_service = ActivityService()

@activity_bp.route('/activity', methods=['POST'])
#@login_required
def create_activity():
    data = request.get_json()    
    activity_id = activity_service.create_activity(data.get('name'), data.get('lessons_id'), data.get('activity_details'))
    return jsonify({'activity_id': str(activity_id)}), 201


@activity_bp.route('/activity/<activity_id>', methods=['GET'])
#@login_required
def get_activity(activity_id):
    activity = activity_service.get_activity(activity_id)
    if activity:
        return jsonify(activity), 200
    else:
        return jsonify({"message": "Activity not found"}), 404


@activity_bp.route('/activity/<activity_id>', methods=['PUT'])
#@login_required
def update_activity(activity_id):
    activity_data = request.json
    updated_count = activity_service.update_activity(activity_id, activity_data)
    if updated_count > 0:
        return jsonify({"message": "Activity updated successfully"}), 200
    else:
        return jsonify({"message": "Activity not found"}), 404


@activity_bp.route('/activity/<activity_id>', methods=['DELETE'])
#@login_required
def delete_activity(activity_id):
    deleted_count = activity_service.delete_activity(activity_id)
    if deleted_count > 0:
        return jsonify({"message": "Activity deleted successfully"}), 200
    else:
        return jsonify({"message": "Activity not found"}), 404