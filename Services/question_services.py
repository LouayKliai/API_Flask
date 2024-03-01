# from Models.question_model import Question
from Models.question_model import Question
class QuestionService:
    def create_question(self, number, question_id, question_text, options, correction_option):
        question = Question(number=number, question_id=question_id, question_text=question_text, option=options, correction_option=correction_option)
        question.save()
        return str(question.id)

    def get_question(self, question_id):
        question = Question.objects(id=question_id).first()
        return question.to_json() if question else None

    def update_question(self, question_id, data):
        question = Question.objects(id=question_id).first()
        if question:
            question.modify(**data)
            return True
        return False

    def delete_question(self, question_id):
        question = Question.objects(id=question_id).first()
        if question:
            question.delete()
            return True
        return False
