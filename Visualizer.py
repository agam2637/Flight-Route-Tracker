import folium
from folium.plugins import AntPath

map_obj = folium.Map(location=[56.1304, -106.3468], zoom_start=5)

pathlatlngs = [(43.677700, -79.624800), (49.194700, -123.179200)]

AntPath(pathlatlngs, delay=400, weight=8, color="red", pulse_color="orange",
        dash_array=[30, 15]).add_to(map_obj)

map_obj.save("routes2.html")

"""
map_obj = folium.Map(location=[56.1304, -106.3468], zoom_start=5)

pathLatLngs = [(19.082502, 72.7163773), (12.9541467, 77.3191065),
               (23.199546, 77.3234906), (19.0860154, 82.0145882),
               (22.5355649, 88.2649519)]

AntPath(pathLatLngs, delay=400, weight=8, color="blue", pulse_color="orange",
        dash_array=[30, 15]).add_to(map_obj)

map_obj.save("routes.html")
"""
