from flask import Flask
import os

def create_app():
    app = Flask(__name__)

    from flask_wtf.csrf import CSRFProtect
    csrf = CSRFProtect()
    csrf.init_app(app)
    app.config['SECRET_KEY'] = os.environ.get('HIDDEN_SECRET_KEY')

    from cache.cache import cache
    cache.init_app(app)

    from database.createdata import create_collection
    create_collection()

    from view.home.home import homeday
    from view.fishdata.map_blueprint import map_blueprint
    from view.fishdata.fishy_catch import fishy_catch
    from view.fishdata.fishy_worker import fishy_worker
    from view.about.about import aboutfishery
    from view.other.other import other
    from view.information.callme import callme
    from view.information.aboutme import aboutme
    app.register_blueprint(homeday)
    app.register_blueprint(map_blueprint,url_prefix='/map_blueprint')
    app.register_blueprint(fishy_catch,url_prefix='/fishy_catch')
    app.register_blueprint(fishy_worker,url_prefix='/fishy_worker')
    app.register_blueprint(aboutfishery,url_prefix='/about')
    app.register_blueprint(other,url_prefix='/other')
    app.register_blueprint(callme,url_prefix='/callme')
    app.register_blueprint(aboutme,url_prefix='/aboutme')

    return app