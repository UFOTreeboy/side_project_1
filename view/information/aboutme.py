from flask import  render_template, Blueprint, request, redirect, url_for
from database.database import connect_to_mongodb

aboutme = Blueprint('aboutme',__name__,
                    template_folder= 'templates',)

@aboutme.route("/aboutme",methods=['GET'])
def about_me():
    return render_template('information/aboutme.html')
