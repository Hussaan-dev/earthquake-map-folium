import pandas as pd
import folium
from folium.plugins import MarkerCluster

d=pd.read_csv('earthquakes.csv')

def colorcheck(magnitude):
    if magnitude < 3.0:
        return 'green'
    elif magnitude < 5.0:
        return 'orange'
    elif magnitude < 6.0:
        return 'red'
    elif magnitude < 7.0:
        return 'darkred'
    else:
        return 'black'
    
lat=list(d['LAT'])
lon=list(d['LON'])
mag=list(d['MAG'])
plc=list(d['Place'])
time=list(d['Time'])

html= ''' <h4> Earthquake information: </h4>
<b> Magnitude:</b> %s <br>
<b> Place:</b> %s <br>
<b> Time:</b> %s 
'''

map=folium.Map(location=[41.0082,28.9784],zoom_start=6,tiles='OpenStreetMap')

fgp=folium.FeatureGroup(name='Tectonic Plates')

fgp.add_child(folium.GeoJson(data=open('plates.json','r',encoding='utf-8-sig').read()
,style_function= lambda x: {'color': 'orange', 'weight': 3, 'dashArray' :'5,5'}))

fge=folium.FeatureGroup(name='Earthquakes')
marker_cluster=MarkerCluster().add_to(fge)

for lt,ln,mg,pl,t in zip(lat,lon,mag,plc,time):
    iFrame=folium.IFrame(html= html % (mg,pl,t),width=250,height= 100 )
    folium.Marker(location=[lt,ln],popup=folium.Popup(iFrame),
    icon=folium.Icon(icon='flash', color=colorcheck(mg))).add_to(marker_cluster)
map.add_child(fgp)
map.add_child(fge)
map.add_child(folium.LayerControl())
map.save('earthquake.html')
