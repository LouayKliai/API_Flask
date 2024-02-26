from flask import Flask, jsonify, request,Blueprint
from Models.lesson_model import Lesson
from Services.lesson_services import LessonService

curriculum_bp = Blueprint('curriculum_bp', __name__)

lesson = Lesson("Title", "Content")

@curriculum_bp.route('/lesson/question', methods=['POST'])
def add_question():
    data = request.json
    question = data.get('question')
    if not question:
        return jsonify({'error': 'Question is required'}), 400
    LessonService.add_question(lesson, question)
    return jsonify({'message': 'Question added successfully'}), 201

@curriculum_bp.route('/lesson/activity', methods=['POST'])
def add_activity():
    data = request.json
    activity = data.get('activity')
    if not activity:
        return jsonify({'error': 'Activity is required'}), 400
    LessonService.add_activity(lesson, activity)
    return jsonify({'message': 'Activity added successfully'}), 201

@curriculum_bp.route('/lesson/resource', methods=['POST'])
def add_resource():
    data = request.json
    resource = data.get('resource')
    if not resource:
        return jsonify({'error': 'Resource is required'}), 400
    LessonService.add_resource(lesson, resource)
    return jsonify({'message': 'Resource added successfully'}), 201

@curriculum_bp.route('/lesson/details', methods=['GET'])
def get_lesson_details():
    return jsonify(LessonService.get_lesson_details(lesson))
