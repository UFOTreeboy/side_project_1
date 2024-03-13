from flask import  render_template, Blueprint
import base64
from io import BytesIO
from matplotlib.figure import Figure

fishy_worker = Blueprint('fishy_worker',__name__,
                template_folder= 'templates',
                static_folder='static')

@fishy_worker.route("/",methods=['GET'])
def worker():
    fig = Figure()
    ax = fig.subplots()
    ax.plot([1, 2])
    buf = BytesIO()
    fig.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template("fishy/fishy_worker.html",data=data)


    #f"<img src='data:image/png;base64,{data}'/>"