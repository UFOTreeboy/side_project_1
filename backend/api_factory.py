from flask import Flask

def create_app():
    app = Flask(__name__)

    
    from backend.map.map_blueprint import map_blueprint

    
    app.register_blueprint(map_blueprint,url_prefix='/')

    from .cache.cache import cache

    cache.init_app(app)

    return app