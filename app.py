from flask import Flask
from Controllers.curriculum_controller import curriculum_bp
from Controllers.lesson_controllers import lesson_bp
from controllers.module_controller import module_bp
from controllers.user_controller import user_bp
from controllers.school_controller import school_bp
app = Flask(__name__)


app.register_blueprint(curriculum_bp)
app.register_blueprint(lesson_bp)
app.register_blueprint(module_bp)
app.register_blueprint(user_bp)
app.register_blueprint(school_bp)




if __name__ == '__main__':
    app.run()
