from flask import  render_template, Blueprint

aboutfishery = Blueprint('aboutfishery',__name__,
                template_folder= 'templates',
                            )

@aboutfishery.route("/about",methods=['GET'])
def about_html():
    return render_template('about/aboutfishery.html')

@aboutfishery.route("/law",methods=['GET'])
def law_html():
    return render_template('about/aboutlaw.html')

 
@aboutfishery.route("/dilemma",methods=['GET'])
def dilemma_html():
    return render_template('about/aboutdilemma.html')