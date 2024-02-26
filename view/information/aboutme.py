from flask import  render_template, Blueprint, request, redirect, url_for
from database.database import connect_to_mongodb

aboutme = Blueprint('aboutme',__name__,
                    template_folder= 'templates',)

@aboutme.route("/taiwan_moa",methods=['GET'])
def about_me():
    return render_template('information/aboutme.html')

@aboutme.route("/call_me",methods=['POST'])
def call_me():
    database_name = 'treeboy'
    collection_name = 'a_users'
    data_collection = connect_to_mongodb(database_name, collection_name)

    name = request.form.get('name')
    profession = request.form.get('profession')
    text = request.form.get('text')

    
    if data_collection.name != collection_name:
        data_collection = connect_to_mongodb(database_name, collection_name)

        new_data = {
        "name": name,
        "profession": profession,
        "text": text
        }
    data_collection.insert_one(new_data)

    return redirect(url_for('aboutme.about_me'))