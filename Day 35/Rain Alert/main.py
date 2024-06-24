import requests
from twilio.rest import Client


OEM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "df18baaf45770a059a77fb249224c13d"
api_key2 = "a2376864b3c876ea817f41d61a19c096"
api_key3 = "c76db73510bd8a07647f8cfdff87fb66"
account_sid = "ACde6a306d91521b0dad494b984f42beea"
auth_Token = "1533eabe1b7d6a4db613a6f4ce1830fc"


weather_params = {
    "lat": 51.759850,
    "lon": 19.458600,
    "appid": "08d1e03a31c8bb772eb866284ca81346",
    "exclude": "current,minutely,daily"
}

response = requests.get(OEM_Endpoint, params=weather_params)
print(response)
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True


if will_rain:
    client = Client(account_sid, auth_Token)
    message = client.messages \
        .create(
        body="Bring your umbrella ☔☔.",
        from_="+16165233176",
        to="+2349134710006"
    )

    print(message.status)

