import requests
from datetime import datetime
import os

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/6f6c19c750f8c976aff5ad60b226ef23/workoutTracking/workouts"


APPLICATION_ID = "169d0197"
APPLICATION_KEYS = "53be3dc43f313af4fd6e4aec24de91f4"




HEADER = {
    "x-app-id": APPLICATION_ID,
    "x-app-key": APPLICATION_KEYS
}

EXERCISE_PARAMETERS = {
    "query": input("Tell me which exercise you did: "),
    "gender": "male",
    "weight_kg": 106,
    "height_cm": 194,
    "age": 24
}




response = requests.post(url=EXERCISE_ENDPOINT, json=EXERCISE_PARAMETERS, headers=HEADER)
results = response.json()
print(results)


Date = datetime.now().strftime("%d/%m/%Y")
Time = datetime.now().strftime("%X")


for exercise in results["exercises"]:
    SHEETY_PARAMETERS = {
        "workout": {
            "date": Date,
            "time": Time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }


Headers = {
    "Authorization": "Bearer Boluwatito17!"
}

sheet_response = requests.post(url=SHEETY_ENDPOINT, json=SHEETY_PARAMETERS, headers=Headers)
print(sheet_response.text)
