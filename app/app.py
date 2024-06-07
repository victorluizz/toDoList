from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:14032000@localhost/db_ToDoList'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    db.init_app(app)

    with app.app_context():
        db.create_all()

    from routes import bp_membros, bp_tarefas
    app.register_blueprint(bp_membros, url_prefix='/')
    app.register_blueprint(bp_tarefas, url_prefix='/')

    return app
