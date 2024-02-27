# services/topic_service.py
from Models.topic_model import Topic  # Assuming you have the Topic model
from db import topics_collection  # Assuming you have the topics_collection

class TopicService:
    @staticmethod
    def topic_exists_by_name(name):
        return topics_collection.find_one({'name': name}) is not None

    @staticmethod
    def create_topic(name, description, lessons=[]):
        if not name:
            raise ValueError('Topic name is required for creating a topic.')

        if TopicService.topic_exists_by_name(name):
            raise ValueError('A topic with this name already exists.')

        new_topic = Topic(name, description, lessons)
        topics_collection.insert_one(new_topic.__dict__)
        return new_topic

    @staticmethod
    def get_topics():
        # Add your logic to retrieve topics from the database
        # For example, you may use an ORM like SQLAlchemy or MongoDB driver
        topics = []  # Replace with actual retrieval logic
        return topics
