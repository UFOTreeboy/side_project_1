from flask import Flask


def create_app():
    app = Flask(__name__)

    from cache.cache import cache
    cache.init_app(app)

    from view.home.home import homeday
    from view.fishdata.map_blueprint import map_blueprint
    from view.about.about import aboutfishery
    from view.other.other import other
    app.register_blueprint(homeday)
    app.register_blueprint(map_blueprint,url_prefix='/map_blueprint')
    app.register_blueprint(aboutfishery,url_prefix='/about')
    app.register_blueprint(other,url_prefix='/other')


    return app