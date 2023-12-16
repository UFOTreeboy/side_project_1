import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from flask import Flask, render_template
from io import BytesIO
import base64


app = Flask(__name__)

@app.route('/')
def plot():


    img = BytesIO()


    a_dictionary = {"a": 4, "b": 20, "c": 6}
    keys = a_dictionary.keys()
    values = a_dictionary.values()
    plt.bar(keys, values)

    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')

    return render_template('catch.html', plot_url=plot_url)

if __name__ == '__main__':
    app.run()