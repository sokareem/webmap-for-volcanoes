#Writing a basemap by Sinmisola Kareem
import folium
import pandas

#create dataframe object
data = pandas.read_csv("Volcanoes.txt")
lon = list(data["LON"]) #List of Longitudes
lat = list(data["LAT"]) # List of Latitudes
elev = list(data["ELEV"]) # list of all elevations

#Color producer in accordance to elevation
def color_producer(elevation):
  if(elevation < 1000):
    return 'green'
  elif( 1000 <= elevation < 3000):
    return 'orange'
  else:
    return 'red'


#Create the map object
map = folium.Map(location=[38.59, -99.09], zoom_start=6, tiles="Mapbox Bright")

#Add markers (points on the map)
#Create a feature group
fg_v = folium.FeatureGroup(name="Volcanoes")# you can add multiple features

for lt, ln, el in zip(lat,lon,elev):
  #change marker to a circle
  fg_v.add_child(folium.CircleMarker(location=[lt,ln], radius= 7, popup = str(el)+" m", fill_color=color_producer(el), color = 'grey', fill=True, fill_opacity = 0.7))
  # default marker = fg.add_child(folium.Marker(location=[lt,ln], popup=str(el), icon= folium.Icon(color = color_producer(el))))

fg_p = folium.FeatureGroup(name="Populations")
# GeoJSON object world.json classification algorithmsa
# style function expects a lambda function to fill in a color_producer function with respect to population size
fg_p.add_child(folium.GeoJson(data=open('world.json','r', encoding='utf-8-sig').read(),style_function= lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

# ADDING A LAYER CONTROL and FEATURE GROUP
map.add_child(fg_p)
map.add_child(fg_v)
map.add_child(folium.LayerControl())

map.save("Map1.html")
