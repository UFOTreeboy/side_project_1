from flask import  render_template, Blueprint

homeday = Blueprint('homeday',__name__,
                    template_folder= 'templates',)

@homeday.route("/",methods=['GET'])
def index():
    return render_template('home/home.html')