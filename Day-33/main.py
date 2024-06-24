import requests
from datetime import datetime
MY_LAT = 7.150130
MY_LNG = 3.346030
ON = 1
OFF = 0
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# iss_position = (longitude, latitude)
# print(iss_position)

parameter = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": OFF
}


response = requests.get("https://api.sunrise-sunset.org/json", params=parameter)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)
time_now = datetime.now()
print(time_now.hour)