import requests
from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "boluwatito"
TOKEN = "Boluwatito17!"


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

GRAPH_PARAMS = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "mins",
    "type": "int",
    "color": "sora",
    "timezone": "UTC"

}

headers = {
    "X-USER-TOKEN": TOKEN

}

# response = requests.post(url=GRAPH_ENDPOINT, json=GRAPH_PARAMS, headers=headers)
# print(response.text)

PIXEL_POST_ENDPOINT = f"{GRAPH_ENDPOINT}/graph1"

today = datetime.now()
TODAY = today.strftime("%Y%m%d")

PIXEL_CONFIG = {
    "date": TODAY,
    "quantity": input("How long did you code for today?: ")

}

response = requests.post(url=PIXEL_POST_ENDPOINT, json=PIXEL_CONFIG, headers=headers)
print(response.text)

PIXEL_PUT_ENDPOINT = f"{PIXEL_POST_ENDPOINT}/{TODAY}"

PUT_CONFIG = {
    "quantity": "60"
}

# response = requests.put(url=PIXEL_PUT_ENDPOINT, json=PUT_CONFIG, headers=headers)
# print(response.text)

PIXEL_DELETE_ENDPOINT = f"{PIXEL_POST_ENDPOINT}/{TODAY}"

# response = requests.delete(url=PIXEL_DELETE_ENDPOINT, headers=headers)
# print(response.text)