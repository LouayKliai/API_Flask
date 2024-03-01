from mongoengine import connect

def initialize_db():
    connect(
        db='Adaptive_learning',
        host='mongodb+srv://admin:louay@cluster0.g7oulyh.mongodb.net/'
    )





# from pymongo import MongoClient
# client = MongoClient('mongodb+srv://admin:louay@cluster0.g7oulyh.mongodb.net/')
# db = client['Adaptive_learning']
# activity_collection=db['activity']
# curriculum_collection = db['curriculums']
# grade_collection = db['grade']
# lesson_collection = db['lessons']
# question_collection = db['question']
# ressource_collection = db['ressource']
# school_collection = db['schools']
# subject_collection = db['subject']
# topic_collection = db['topic']
# user_collection = db['users']

