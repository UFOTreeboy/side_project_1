from flask import Flask, render_template, Blueprint
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import base64


taiwan_catch = Blueprint('taiwan_catch', __name__)

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

@taiwan_catch.route("/")
def fullscreen():
    fig, ax = plt.subplots()
    ax.plot(xpoints, ypoints)

    img_buf = BytesIO()
    fig.savefig(img_buf, format='png')
    img_buf.seek(0)

    encoded_img = base64.b64encode(img_buf.read()).decode('utf-8')

    plt.close(fig)

    return render_template('catch.html', chart=encoded_img)



