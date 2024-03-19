from flask import  render_template, Blueprint, request, redirect, url_for, flash
from database.database import connect_to_mongodb
from database.form import MyForm


callme = Blueprint('callme',__name__,
                    template_folder= 'templates',)

db = connect_to_mongodb('new_users')

@callme.route("/callme",methods=['GET','POST'])
def call_me():
    form = MyForm()
    if form.validate_on_submit():
        profession = request.form['profession']
        content = request.form["content"]
        db.insert_one({'profession':profession , 'content': content})
        flash('資料已經送出囉!', 'success')
        return redirect(url_for('callme.call_me'))
    return render_template('information/callme.html',form=form)