from flask import Flask, app
from flask_sqlalchemy import SQLAlchemy
from os import path

app = Flask(__name__)
db = SQLAlchemy(app)
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db = SQLAlchemy(app)
    db.init_app(app)

    

    from .hospital_reg import hospital_reg
    from .home import home
    from .user_info import info
    from .message import message

    app.register_blueprint(hospital_reg, url_prefix='/')
    app.register_blueprint(home, url_prefix='/')
    app.register_blueprint(info, url_prefix='/')
    app.register_blueprint(message, url_prefix='/')

    from .models import Hospital

    create_database(app)
    
    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app = app)
        print('Created Database!')