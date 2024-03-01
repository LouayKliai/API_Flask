from mongoengine import Document, StringField, ListField
#from dataBase import 
class Question(Document):
    number = StringField(required=True)
    question_id = StringField(required=True)
    question_text = StringField(required=True)
    option = ListField(StringField())
    correction_option = StringField(required=True)


# class Question(Document):
#     number = StringField(required=True)
#     question_id = StringField(required=True)
#     question_text = StringField(required=True)
#     option = ListField(StringField())
#     correction_option = StringField(required=True)
