from flask import  render_template, Blueprint

aboutfishery = Blueprint('aboutfishery',__name__,
                template_folder= 'templates',
                            )

@aboutfishery.route("/")
def about_html():
    return render_template('about/aboutfishery.html')

