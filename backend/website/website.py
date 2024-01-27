from flask import Blueprint,render_template

website = Blueprint('website',__name__)

@website.route("/")
def hello_world():
    return render_template('index.html')

