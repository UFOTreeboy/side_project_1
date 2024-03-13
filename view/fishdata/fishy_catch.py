from flask import  render_template, Blueprint
import base64
from io import BytesIO
from matplotlib.figure import Figure

fishy_catch = Blueprint('fishy',__name__,
                template_folder= 'templates',
                static_folder='static')

@fishy_catch.route("/",methods=['GET'])
def hello():
    fig = Figure()
    ax = fig.subplots()
    ax.plot([1, 2])
    buf = BytesIO()
    fig.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template("fishy/fishy_catch.html",data=data)


    #f"<img src='data:image/png;base64,{data}'/>"