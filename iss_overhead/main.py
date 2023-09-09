import requests
import time
from datetime import datetime
from smtplib import SMTP


MY_LAT = 7.150130
MY_LONG = 3.346030
MY_POSITION = (MY_LONG, MY_LAT)
USERNAME = "adesanyaboluwatito69@gmail.com"
PASSWORD = "Boluwatito17!"


def plus_or_minus_location():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    responses = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    responses.raise_for_status()
    datas = responses.json()
    sunrise = int(datas["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(datas["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    # if it is dark
    if sunset <= time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    # and it is currently dark
    # Then email me to tell me to look up.
    # BONUS: run the code every 60 seconds.
    if plus_or_minus_location() and is_night():
        with SMTP(host="stmp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=USERNAME, password=PASSWORD)
            connection.sendmail(from_addr=USERNAME,
                                to_addrs="boluwatitoadesanya@gmail.com",
                                msg=f"Subject:Look up!\n\nISS is above you"
                                )
