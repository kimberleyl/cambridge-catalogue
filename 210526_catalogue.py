#imports
import folium
import webbrowser
import csv

#create catalogue
catalogue = []

#read items csv
with open("items.csv",mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        item = {}
        item["latitude"] = row["latitude"]
        item["longitude"] = row["longitude"]
        item["name"] = row["name"]
        catalogue.append(item)

#create map
map = folium.Map(location=[52.2088214,0.1199476], zoom_start=14)

#add markers
for item in catalogue:
    folium.Marker([item["latitude"],item["longitude"]], popup = item["name"]).add_to(map)

#display map
filepath = "C:/Users/USER/OneDrive - The Chinese University of Hong Kong/CODING/210526_catalogue/map.html"
map.save(filepath)
webbrowser.open(filepath)
