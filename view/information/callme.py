from flask import  render_template, Blueprint


callme = Blueprint('callme',__name__,
                    template_folder= 'templates',)



@callme.route("/callme",methods=['GET','POST'])
def call_me():

    return render_template('information/callme.html')