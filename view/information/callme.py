from flask import  render_template, Blueprint,request
from database.database import connect_to_mongodb


callme = Blueprint('callme',__name__,
                    template_folder= 'templates',)

db = connect_to_mongodb('treeboy', 'new_users')

@callme.route("/callme",methods=['GET','POST'])
def call_me():
    if request.method=='POST':
        name = request.form['name']
        profession = request.form['profession']
        text = request.form["text"]
        db.insert_one({'name':name , 'profession':profession , 'text': text})
    return render_template('information/callme.html')