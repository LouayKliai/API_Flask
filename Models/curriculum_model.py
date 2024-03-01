from mongoengine import Document, StringField, ReferenceField,ListField

class Curriculum(Document):
    name = StringField(required=True)
    grades = ListField(ReferenceField('Grade'))
    subjects = ReferenceField('Subject')
    #subjects = ListField(ReferenceField('Subject'))

    # def add_grade(self, grade):
    #     self.grades.append(grade)

    # def add_subject(self, subject):
    #     self.subjects.append(subject)