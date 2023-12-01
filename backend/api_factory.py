from flask import Flask

def creat_app():
    app = Flask(__name__)

    from backend.website.website import website
    from backend.map.map import map

    app.register_blueprint(website,url_prefix='/')
    app.register_blueprint(map)

    return app