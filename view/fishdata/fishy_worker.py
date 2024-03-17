from flask import  render_template, Blueprint
from database.database import connect_to_mongodb
import base64
from io import BytesIO
from matplotlib.figure import Figure
import seaborn as sns
import pandas as pd


fishy_worker = Blueprint('fishy_worker',__name__,
                template_folder= 'templates',
                static_folder='static')

data_collection = connect_to_mongodb('treeboy', 'fisky_work_ocean')
cl = pd.DataFrame(list(data_collection.find()))


@fishy_worker.route("/",methods=['GET'])
def worker():
    





    fig = Figure(figsize=(10, 5.2))
    ax = fig.subplots()
    x_sorted = cl['date']
    y_sorted = cl['value']
    ax.plot(x_sorted, y_sorted)
    buf = BytesIO()
    fig.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template("fishy/fishy_worker.html",data=data)


    #f"<img src='data:image/png;base64,{data}'/>"