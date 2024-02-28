from flask import Blueprint, jsonify, request
from Services.question_services import questionService 

question_bp = Blueprint('question_bp', __name__)
question_service = questionService()

@question_bp.route('/question', methods=['POST'])
def create_question():
    data = request.json
    question_id = question_service.create_question(data.get('number'), data.get('question_id'), data.get('question_text'), data.get('options'), data.get('correction_option'))
    return jsonify({"question_id": str(question_id)}), 201

@question_bp.route('/question/<question_id>', methods=['GET'])
def get_question(question_id):
    question = question_service.get_question(question_id)
    if question:
        return jsonify(question), 200
    else:
        return jsonify({"message": "Question not found"}), 404

@question_bp.route('/question/<question_id>', methods=['PUT'])
def update_question(question_id):
    data = request.json
    updated_count = question_service.update_question(question_id, data.get('number'), data.get('question_text'), data.get('options'), data.get('correction_option'))
    if updated_count > 0:
        return jsonify({"message": "Question updated successfully"}), 200
    else:
        return jsonify({"message": "Question not found"}), 404

@question_bp.route('/question/<question_id>', methods=['DELETE'])
def delete_question(question_id):
    deleted_count = question_service.delete_question(question_id)
    if deleted_count > 0:
        return jsonify({"message": "Question deleted successfully"}), 200
    else:
        return jsonify({"message": "Question not found"}), 404
