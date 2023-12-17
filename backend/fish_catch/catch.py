from flask import Blueprint, render_template
import requests


fish_catch = Blueprint('catch', __name__,
                template_folder= 'templates')

def get_data():
    url = "https://data.moa.gov.tw/Service/OpenData/FaRss.aspx?key=073&$top=1000&$skip=0&UnitId=C71"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Can't get data!")

@fish_catch.route('/', methods=['GET', 'POST'])
def fish():
    fish_data = get_data()
    return render_template('catch.html',fish_data=fish_data)
