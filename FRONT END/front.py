from flask import Flask, render_template, json
from datetime import datetime
import requests

app = Flask(__name__)


@app.route('/')
def hello_world(temp=None, latitude=None, longitude=None, contents=None, humidity=None, days=None):
    response = requests.get('https://ip.xila.me/json')
    content = json.loads(response.content.decode('utf-8'))
    lat = content['latitude']
    lon = content['longitude']
    response = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat=49.38241&lon=1.07442&appid=5de5e01c90817ad8fa49b570d672f7ff")
    content = json.loads(response.content.decode('utf-8'))
    daily = content['daily']
    day = []
    for contents in daily:
        if contents["dt"]:
            day.append({"date": datetime.fromtimestamp(contents["dt"]).strftime("%A")})

    return render_template("index.html", latitude=lat, longitude=lon, contents=daily, days=
    day)
