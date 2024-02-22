from flask import  render_template, Blueprint

aboutme = Blueprint('aboutme',__name__,
                    template_folder= 'templates',)

@aboutme.route("/taiwan_moa",methods=['GET'])
def about_me():
    return render_template('information/aboutme.html')

@aboutme.route("/call_me",methods=['GET'])
def call_me():
    return render_template('information/callme.html')