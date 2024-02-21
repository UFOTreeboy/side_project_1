from flask import Flask


def create_app():
    app = Flask(__name__)

    from .cache.cache import cache
    cache.init_app(app)

    from backend.map.home import homeday
    from backend.map.map_blueprint import map_blueprint
    from backend.website.website import website
    from backend.map.about import aboutfishery
    app.register_blueprint(homeday)
    app.register_blueprint(map_blueprint,url_prefix='/map_blueprint')
    app.register_blueprint(website,url_prefix='/website')
    app.register_blueprint(aboutfishery,url_prefix='/about')


    return app