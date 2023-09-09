import requests
from pprint import pprint
SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/6f6c19c750f8c976aff5ad60b226ef23/myFlightDocuments/prices"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        pprint(data)
        return self.destination_data


    def update_destination_code(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )

            print(response.text)
    #This class is responsible for talking to the Google Sheet.
