from flask import Blueprint, jsonify, request
from Services.topic_services import TopicService  # Assuming you have a service for Topic

topic_bp = Blueprint('topic_bp', __name__)

@topic_bp.route('/api/topics', methods=['POST'])
def add_topic_route():
    topic_data = request.json
    name = topic_data.get('name')
    description = topic_data.get('description')
    lessons = topic_data.get('lessons', [])  # Default to an empty list if not provided

    try:
        new_topic = TopicService.create_topic(name, description, lessons)
        return jsonify({'message': 'Topic added successfully', 'topic': new_topic.__dict__}), 201
    except ValueError as e:
        return jsonify({'message': str(e)}), 400

@topic_bp.route('/api/topics', methods=['GET'])
def get_topics_route():
    # Implement logic to retrieve topics from the database
    topics = TopicService.get_topics()  # Replace with actual retrieval logic
    return jsonify({'topics': topics})
