from flask import Blueprint, jsonify, request
from Services.topic_services import TopicService 

topic_bp = Blueprint('topic_bp', __name__)
topic_service = TopicService()

@topic_bp.route('/topic', methods=['POST'])
def create_topic():
    data = request.json
    topic_id = topic_service.create_topic(data.get('name'), data.get('description'), data.get('lessons'))
    return jsonify({"topic_id": str(topic_id)}), 201

@topic_bp.route('/topic/<topic_id>', methods=['GET'])
def get_topic(topic_id):
    topic = topic_service.get_topic(topic_id)
    if topic:
        return jsonify(topic), 200
    else:
        return jsonify({"message": "Topic not found"}), 404

@topic_bp.route('/topic/<topic_id>', methods=['PUT'])
def update_topic(topic_id):
    data = request.json
    updated_count = topic_service.update_topic(topic_id, data.get('name'), data.get('description'), data.get('lessons'))
    if updated_count > 0:
        return jsonify({"message": "Topic updated successfully"}), 200
    else:
        return jsonify({"message": "Topic not found"}), 404

@topic_bp.route('/topic/<topic_id>', methods=['DELETE'])
def delete_topic(topic_id):
    deleted_count = topic_service.delete_topic(topic_id)
    if deleted_count > 0:
        return jsonify({"message": "Topic deleted successfully"}), 200
    else:
        return jsonify({"message": "Topic not found"}), 404
