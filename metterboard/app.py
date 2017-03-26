from flask import Flask

from .backend import backend

DEFAULT_BLUEPRINTS = (
    backend,
)

def create_app():
    app = Flask(__name__)
    configure_blueprints(app, DEFAULT_BLUEPRINTS)
    return app

def configure_blueprints(app, blueprints):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)
