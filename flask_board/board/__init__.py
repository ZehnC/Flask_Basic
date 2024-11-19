from flask import Flask

from board import pages, posts

#Creates Application (application factory)
def create_app():
    app = Flask(__name__)

    app.register_blueprint(pages.bp)

    app.register_blueprint(posts.bp)

    return app