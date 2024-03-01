from Models.topic_model import Topic

class TopicService:
    def create_topic(self, name, description):
        topic = Topic(name=name, description=description)
        topic.save()
        return str(topic.id)

    def get_topic(self, topic_id):
        topic = Topic.objects(id=topic_id).first()
        return topic.to_json() if topic else None

    def update_topic(self, topic_id, data):
        topic = Topic.objects(id=topic_id).first()
        if topic:
            topic.modify(**data)
            return True
        return False

    def delete_topic(self, topic_id):
        topic = Topic.objects(id=topic_id).first()
        if topic:
            topic.delete()
            return True
        return False
