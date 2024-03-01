from Models.activity_model import Activity

class ActivityService:
    def create_activity(self, name, lesson_id, activity_details=None):
        activity = Activity(name=name, lesson_id=lesson_id, activity_details=activity_details)        
        activity.save()
        return str(activity.id)

    def get_activity(self, activity_id):
        activity = Activity.objects(id=activity_id).first()
        return activity.to_json() if activity else None

    def update_activity(self, activity_id, data):
        activity = Activity.objects(id=activity_id).first()
        if activity:
            activity.modify(**data)
            return True
        return False

    def delete_activity(self, activity_id):
        activity = Activity.objects(id=activity_id).first()
        if activity:
            activity.delete()
            return True
        return False
