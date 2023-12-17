from flask import Flask

def create_app():
    app = Flask(__name__)

    from .cache.cache import cache
    cache.init_app(app)

    from backend.website.website import website
    from backend.map.map_blueprint import map_blueprint
    from backend.fish_catch.catch import fish_catch
    app.register_blueprint(website,url_prefix='/website')
    app.register_blueprint(map_blueprint,url_prefix='/map')
    app.register_blueprint(fish_catch,url_prefix='/catch')

    return app