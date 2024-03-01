from flask import Flask, jsonify, request,Blueprint
from Models.lesson_model import Lesson
from Services.lesson_services import LessonService

lesson_bp = Blueprint('lesson_bp', __name__)
lesson_service = LessonService()

@lesson_bp.route('/lesson', methods=['POST'])
def create_lesson():
    data = request.json
    #lesson_id = lesson_service.create_lesson(data.get('title'), data.get('content'), data.get('resources'), data.get('question'), data.get('activities'))
    lesson_id = lesson_service.create_lesson(data.get('title'), data.get('content'))
    return jsonify({"lesson_id": str(lesson_id)}), 201

@lesson_bp.route('/lesson/<lesson_id>', methods=['GET'])
def get_lesson(lesson_id):
    lesson = lesson_service.get_lesson(lesson_id)
    if lesson:
        return jsonify(lesson), 200
    else:
        return jsonify({"message": "Lesson not found"}), 404

@lesson_bp.route('/lesson/<lesson_id>', methods=['PUT'])
def update_lesson(lesson_id):
    data = request.json
    updated_count = lesson_service.update_lesson(lesson_id, data.get('title'), data.get('content'), data.get('resources'), data.get('question'), data.get('activities'))
    if updated_count > 0:
        return jsonify({"message": "Lesson updated successfully"}), 200
    else:
        return jsonify({"message": "Lesson not found"}), 404

@lesson_bp.route('/lesson/<lesson_id>', methods=['DELETE'])
def delete_lesson(lesson_id):
    deleted_count = lesson_service.delete_lesson(lesson_id)
    if deleted_count > 0:
        return jsonify({"message": "Lesson deleted successfully"}), 200
    else:
        return jsonify({"message": "Lesson not found"}), 404