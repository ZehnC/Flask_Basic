from flask import Flask

from board import pages

#Creates Application (application factory)
def create_app():
    app = Flask(__name__)

    app.register_blueprint(pages.bp)

    return app