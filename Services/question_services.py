# services/question_service.py
from Models.question_model import Question  # Assuming you have the Question model
from db import question_collection  # Assuming you have the question_collection

class QuestionService:
    @staticmethod
    def question_exists_by_id(question_id):
        return question_collection.find_one({'question_id': question_id}) is not None

    @staticmethod
    def create_question(number, question_id, question_text, options, correction_option):
        if not question_id:
            raise ValueError('Question ID is required for creating a question.')

        if QuestionService.question_exists_by_id(question_id):
            raise ValueError('A question with this ID already exists.')

        new_question = Question(number, question_id, question_text, options, correction_option)
        question_collection.insert_one(new_question.__dict__)
        return new_question

    @staticmethod
    def get_questions():
        # Add your logic to retrieve questions from the database
        # For example, you may use an ORM like SQLAlchemy or MongoDB driver
        questions = []  # Replace with actual retrieval logic
        return questions
