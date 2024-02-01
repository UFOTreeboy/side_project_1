from flask import Flask, render_template, Blueprint
from ..database.database import connect_to_mongodb
from ..cache.cache import cache
import folium

map_blueprint = Blueprint('map',__name__,
                template_folder= 'templates')

@map_blueprint.route("/")
@cache.cached(timeout=50)
def fullscreen():
    database_name = 'treeboy'
    collection_name = 'newport'

    data_collection = connect_to_mongodb(database_name, collection_name)
    data = data_collection.find()

    map_blueprint = folium.Map(
        location=[23.97289714436863, 121.58616434318259],
        tiles=None,
        zoom_start=7,
        control_scale=True,
        max_bounds=True
    )

    custom_tiles = {
    "預設地圖": "OpenStreetMap",
    }

    for mapname , tiles in custom_tiles.items():
          folium.TileLayer(
          tiles=tiles,
          name=mapname,
          ).add_to(map_blueprint)
   

    first_class_layer = folium.FeatureGroup(name="第一類漁港")
    second_class_layer = folium.FeatureGroup(name="第二類漁港")
    other_class_layer = folium.FeatureGroup(name="廢止漁港")

    for newport in data:
        lat = newport.get('field006')
        lon = newport.get('field005')
        name = newport.get('field002')
        portclass = newport.get('field003')
        phone = newport.get('field007')
        text = f"漁港名稱: <strong>{name}</strong></br> \
            電話: <strong>{phone}</strong></br> \
            分類:<strong>{portclass}</strong></br> \
            介紹:<strong> </strong>"
        

        if portclass == '第一類':
                color = 'red'
                icon = 'ship'
                layer = first_class_layer
        elif portclass == '第二類':
                color = 'blue'
                icon = 'anchor'
                layer = second_class_layer
        else:
                color = 'black'
                icon = 'window-close'
                layer = other_class_layer

        icon = folium.Icon(color=color,icon=icon,prefix='fa')
        iframeA = folium.IFrame(html=text, width=200, height=250)
        popup = folium.Popup(iframeA, max_width=200)
        folium.Marker(
            location=[lat, lon], 
            popup=popup,
            icon=icon

        ).add_to(layer)
    
    first_class_layer.add_to(map_blueprint)
    second_class_layer.add_to(map_blueprint)
    other_class_layer.add_to(map_blueprint)

    map_blueprint.get_root().width = "750px"
    map_blueprint.get_root().height = "550px"

    folium.LayerControl(collapsed=False).add_to(map_blueprint)

    iframe = map_blueprint.get_root()._repr_html_()


    return render_template("index.html",iframe=iframe)

