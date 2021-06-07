#imports
import folium
import webbrowser
import csv
import base64
import pandas
from folium import IFrame
import requests
import geocoder

#create catalogue
catalogue = []

#read items csv
with open("items.csv", mode="r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    for row in reader:
        item = {}
        item["latitude"] = row["latitude"]
        item["longitude"] = row["longitude"]
        item['name'] = row["name"]
        item["architect"] = row["architect"]
        item["year"] = row["year"]
        item["image"] = row["image"]
        item["description"] = row["description"]
        catalogue.append(item)

#locate user
g = geocoder.ip("me")
user_location = g.latlng
print(user_location)

#create map
map = folium.Map(location=user_location, zoom_start=14)
folium.CircleMarker([user_location[0],user_location[1]], radius=5, color="#0000ff",fill=True, fill_opacity=100).add_to(map)
folium.TileLayer('stamentoner').add_to(map)

#image
html = '<img src="data:image/JPG;base64,{}">'.format
encoded = base64.b64encode(requests.get(item["image"]).content).decode()
iframe = IFrame(html(encoded), width=632+20, height=420+20)
picture = folium.Popup(iframe, max_width=1000)
# "<img src=",item["image"],"height=1420px width=2900px>"

#add markers
popup_ = ('<b>',item['name'],'</b>','<br>',item["year"],'<br>',item["architect"],'<br>',"<img src=",item["image"],"height=1420px width=2900px>",'<br>',item["description"])
for item in catalogue:
    folium.CircleMarker([item["latitude"],item["longitude"]], radius=5, popup=popup_, color="#ff0000",fill=True, fill_opacity=100).add_to(map)

#display map
filepath = "C:/Users/USER/OneDrive - The Chinese University of Hong Kong/CODING/210526_catalogue/map.html"
map.save(filepath)
webbrowser.open(filepath)
