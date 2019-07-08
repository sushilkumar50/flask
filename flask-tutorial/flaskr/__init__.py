import os

from flask import Flask
from . import db

from . import auth


def create_app(test_cofig=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='DEV',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_cofig is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_cofig)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    db.init_app(app)
    @app.route('/hello')
    def hello():
        return 'hello, world!'


    app.register_blueprint(auth.bp)
    return app