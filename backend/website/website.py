from flask import Blueprint


website = Blueprint('website',__name__)

@website.route("/")
def hello_world():

    return f"1234"