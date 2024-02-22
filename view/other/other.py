from flask import  render_template, Blueprint

other = Blueprint('other',__name__,
                    template_folder= 'templates',)

@other.route("/taiwan_moa",methods=['GET'])
def taiwan_moa():
    return render_template('other/taiwanmoa.html')

@other.route("/taiwan_ngo",methods=['GET'])
def taiwan_ngo():
    return render_template('other/taiwanngo.html')