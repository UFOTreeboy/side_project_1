from flask import  render_template, Blueprint
from database.database import connect_to_mongodb
import base64
from io import BytesIO
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
import pandas as pd


fishy_catch = Blueprint('fishy',__name__,
                template_folder= 'templates',
                static_folder='static')

data_collection = connect_to_mongodb('fisky_work_ocean')
cl = pd.DataFrame(list(data_collection.find()))

@fishy_catch.route("/",methods=['GET'])
def hello()->plt:
    fig = Figure()
    fig, ax = plt.subplots(figsize=(10,5.2), facecolor='lightskyblue',
                       layout='constrained')
    ax.set_title('unit(tons)', loc='left', fontstyle='oblique', fontsize='medium')
    plt.ticklabel_format(style='plain', axis='y')
    plt.grid()
    fig.autofmt_xdate()
    x_sorted = cl.sort_values('date', ascending=True)['date']
    value_cl_sorted = cl.sort_values('date')
    y_sorted = value_cl_sorted['value']
    ax.plot(x_sorted, y_sorted)
    buf = BytesIO()
    fig.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template("fishy/fishy_catch.html",data=data)


    #f"<img src='data:image/png;base64,{data}'/>"