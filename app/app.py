from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:14032000@localhost/db_ToDoList'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    db.init_app(app)

    with app.app_context():
        db.create_all()

    from routes import bp_membros, bp_tarefas, bp_tarefas_telas
    app.register_blueprint(bp_membros, url_prefix='/')
    app.register_blueprint(bp_tarefas, url_prefix='/')
    app.register_blueprint(bp_tarefas_telas, url_prefix='/')

    return app
