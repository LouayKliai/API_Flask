from Models.lesson_model import Lesson
class LessonService:
    def create_lesson(self, title, content,resources_list,question_list,activities_list):
        lesson = Lesson(title=title, content=content,resources_list=resources_list,question_list=question_list,activities_list=activities_list)
        lesson.save()
        return str(lesson.id)
   
    def get_lesson(self, lesson_id):
        lesson = Lesson.objects(id=lesson_id).first()
        return lesson.to_json() if lesson else None

    def update_lesson(self, lesson_id, data):
        lesson = Lesson.objects(id=lesson_id).first()
        if lesson:
            lesson.modify(**data)
            return True
        return False

    def delete_lesson(self, lesson_id):
        lesson = Lesson.objects(id=lesson_id).first()
        if lesson:
            lesson.delete()
            return True
        return False
