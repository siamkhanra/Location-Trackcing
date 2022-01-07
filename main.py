import phonenumbers
import opencage
import folium
from phoneno import number 
from phonenumbers import geocoder

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print("Location of the Number is ", location)

from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
service_pro_name = carrier.name_for_number(service_provider, "en")
print("Service Provider Name is ", service_pro_name)

from opencage.geocoder import OpenCageGeocode
key = 'e49fe2e511994ed288fa09cf9323309f'

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
#print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat,lng)

myMap = folium.Map(location = [lat, lng], zoom_start= 9)
folium.Marker([lat, lng], popup = location).add_to(myMap)

myMap.save("myLocation.html")

