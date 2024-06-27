import phonenumbers
import opencage
import folium
from phone_number import number,region_code

from phonenumbers import geocoder

pnumber = phonenumbers.parse(number,region_code)

location = geocoder.description_for_number(pnumber, "en")
print(location)

from phonenumbers import carrier

provider = phonenumbers.parse(number,region_code)
print(carrier.name_for_number(provider,"en"))

from opencage.geocoder import OpenCageGeocode

key = 'caeeb1e96cf546cabb337d865275156b'
geocoder = OpenCageGeocode(key)
query = str(location)

result = geocoder.geocode(query)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']

print(lat,lng)

mymap = folium.Map(location=[lat,lng], zoom_start=9)
folium.Marker([lat,lng],popup=location).add_to(mymap)

mymap.save("myplace.html")
