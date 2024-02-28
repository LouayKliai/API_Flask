from Models.topic_model import Topic
from db import topic_collection 

class TopicService:
    def create_topic(self, name, description, lessons=None):
        topic = Topic(name, description, lessons)
        result = topic_collection.insert_one(topic.__dict__)
        return result.inserted_id

    def get_topic(self, topic_id):
        topic = topic_collection.find_one({"_id": topic_id})
        return topic

    def update_topic(self, topic_id, name=None, description=None, lessons=None):
        update_data = {}
        if name is not None:
            update_data["name"] = name
        if description is not None:
            update_data["description"] = description
        if lessons is not None:
            update_data["lessons"] = lessons
        
        result = topic_collection.update_one({"_id": topic_id}, {"$set": update_data})
        return result.modified_count

    def delete_topic(self, topic_id):
        result = topic_collection.delete_one({"_id": topic_id})
        return result.deleted_count