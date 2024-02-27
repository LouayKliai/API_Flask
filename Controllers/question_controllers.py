from flask import Blueprint, jsonify, request
from Services.question_services import QuestionService  # Assuming you have a service for Question

question_bp = Blueprint('question_bp', __name__)

@question_bp.route('/api/questions', methods=['POST'])
def add_question_route():
    question_data = request.json
    number = question_data.get('number')
    question_id = question_data.get('question_id')
    question_text = question_data.get('question_text')
    options = question_data.get('options')
    correction_option = question_data.get('correction_option')

    try:
        new_question = QuestionService.create_question(number, question_id, question_text, options, correction_option)
        return jsonify({'message': 'Question added successfully', 'question': new_question.__dict__}), 201
    except ValueError as e:
        return jsonify({'message': str(e)}), 400

@question_bp.route('/api/questions', methods=['GET'])
def get_questions_route():
    # Implement logic to retrieve questions from the database
    questions = QuestionService.get_questions()  # Replace with actual retrieval logic
    return jsonify({'questions': questions})
