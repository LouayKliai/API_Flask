from Models.lesson_model import Lesson
from db import lesson_collection 
class LessonService:
    def create_lesson(self, title, content, resources=None, questions=None, activities=None):
        lesson_data = {
            "title": title,
            "content": content,
            "resources": resources,
            "questions": questions,
            "activities": activities
        }
        result = lesson_collection.insert_one(lesson_data)
        return result.inserted_id


    def get_lesson(self, lesson_id):
        lesson = lesson_collection.find_one({"_id": lesson_id})
        return lesson

    def update_lesson(self, lesson_id, title=None, content=None, resources=None, questions=None, activities=None):
        update_data = {}
        if title is not None:
            update_data["title"] = title
        if content is not None:
            update_data["content"] = content
        if resources is not None:
            update_data["resources"] = resources
        if questions is not None:
            update_data["question"] = questions
        if activities is not None:
            update_data["activities"] = activities
        
        result = lesson_collection.update_one({"_id": lesson_id}, {"$set": update_data})
        return result.modified_count

    def delete_lesson(self, lesson_id):
        result = lesson_collection.delete_one({"_id": lesson_id})
        return result.deleted_count
