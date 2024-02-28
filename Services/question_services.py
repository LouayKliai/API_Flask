from Models.question_model import question
from db import question_collection 
class questionService:
    def create_question(self, number, question_id, question_text, options, correction_option):
        Question = question(number, question_id, question_text, options, correction_option)
        result = question_collection.insert_one(Question.__dict__)
        return result.inserted_id

    def get_question(self, question_id):
        question = question_collection.find_one({"question_id": question_id})
        return question

    def update_question(self, question_id, number=None, question_text=None, options=None, correction_option=None):
        update_data = {}
        if number is not None:
            update_data["number"] = number
        if question_text is not None:
            update_data["question_text"] = question_text
        if options is not None:
            update_data["options"] = options
        if correction_option is not None:
            update_data["correction_option"] = correction_option
        
        result = question_collection.update_one({"question_id": question_id}, {"$set": update_data})
        return result.modified_count

    def delete_question(self, question_id):
        result = question_collection.delete_one({"question_id": question_id})
        return result.deleted_count