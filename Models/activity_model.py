from flask import Flask

class Activity:
     def __init__(self, name,lesson_id,activity_type,activity_details):
        self.name = name
        self.lesson_id=lesson_id        
        self.activity_type=activity_type
        self.activity_details=activity_details

# {
#     _id: ObjectId,
#     lesson_id: ObjectId, // Reference to the lesson
#     activity_type: String, // Type of activity (e.g., 'assignment', 'quiz', 'experiment', etc.)
#     activity_details: Object // Additional details specific to the activity type
# }