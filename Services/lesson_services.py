from Models.lesson_model import Lesson

class LessonService:


    @staticmethod
    def add_question(lesson, question):
        lesson.questions.append(question)
    
    @staticmethod
    def add_activity(lesson, activity):
        lesson.activities.append(activity)
    
    @staticmethod
    def add_resource(lesson, resource):
        lesson.resources.append(resource)

    @staticmethod
    def get_lesson_details(lesson):
        return {
            "title": lesson.title,
            "content": lesson.content,
            "questions": lesson.questions,
            "activities": lesson.activities,
            "resources": lesson.resources
        }
