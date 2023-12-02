from flask import Flask, render_template_string, Blueprint

import folium

map = Blueprint('map',__name__)

@map.route("/map")
def fullscreen():
    m = folium.Map(
        location=[23.97289714436863, 121.58616434318259],
        tiles="OpenStreetMap",
        zoom_start=7,
        control_scale=True,
        max_bounds=True
    )

    
    return m.get_root().render()

