from flask import Blueprint
from backend.map.weather import weather_data

website = Blueprint('website',__name__)

@website.route("/")
def hello_world():

    weather_info = weather_data()
    if weather_info:
        return f"<p>Location: {weather_info['locations']}</p>"
    
    else:
        return "<p>No weather data available</p>"