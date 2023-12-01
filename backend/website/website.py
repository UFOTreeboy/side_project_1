from flask import Blueprint,render_template


website = Blueprint('website',__name__)

@website.route("/")
def hello_world():
    return "<p>Hello, World!</p>"