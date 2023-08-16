import geocoder
import folium

ip_opera = "216.119.34.204 "
ip2 = "107.77.235.236 "
ip3 = " 107.77.68.114 "

g = geocoder.ip(ip_opera)

lat_long = g.latlng

print(f"location: {lat_long}")

map1 = folium.Map(location = lat_long, zoom_start = 12)
folium.CircleMarker(location = lat_long, radius = 50, popup = "found him").add_to(map1)

map1.save("map1.html")