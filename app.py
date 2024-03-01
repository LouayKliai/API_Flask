from flask import Flask
from Controllers.curriculum_controllers import curriculum_bp
from Controllers.lesson_controllers import lesson_bp
from Controllers.activity_controllers import activity_bp
from Controllers.user_controllers import user_bp
from Controllers.school_controllers import school_bp
from Controllers.grade_controllers import grade_bp
from Controllers.question_controllers import question_bp
from Controllers.resource_controllers import resource_bp
from Controllers.subject_controllers import subject_bp
from Controllers.topic_controllers import topic_bp
from db import initialize_db
app = Flask(__name__)
initialize_db()
app.register_blueprint(curriculum_bp)
app.register_blueprint(activity_bp)
app.register_blueprint(grade_bp)
app.register_blueprint(user_bp)
app.register_blueprint(school_bp)
app.register_blueprint(lesson_bp)
app.register_blueprint(question_bp)
app.register_blueprint(resource_bp)
app.register_blueprint(subject_bp)
app.register_blueprint(topic_bp)

if __name__ == '__main__':
    app.run()
