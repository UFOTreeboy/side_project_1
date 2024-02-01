from flask import Flask


def create_app():
    app = Flask(__name__)

    from .cache.cache import cache
    cache.init_app(app)



    from backend.website.website import website
    from backend.map.map_blueprint import map_blueprint
    app.register_blueprint(website,url_prefix='/')
    app.register_blueprint(map_blueprint,url_prefix='/map')


    return app