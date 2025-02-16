import requests
from datetime import datetime
import os 


APP_ID = "id"
API_KEY = "key"
# APP_ID = os.environ["NT_APP_ID"]
# API_KEY = os.environ["NT_API_KEY"]

GENDER = "Male"
WEIGHT_KG =  59
HEIGHT_CM = 179
AGE = 19
# time = datetime.datetime.now()
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Tell me which exercises you did: ")
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}


response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
# print(f"burned {result['exercises'][0]['nf_calories']} calories")

# print(result)

sheety_endpoint =  "https://api.sheety.co/865f7020c6d6b3bd991d00e7bb4e62f5/workoutTracker/workouts"

for exercise in result["exercises"]:
    sheety_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

bearer_headers = { 
    "Authorization":"Bearer xxxxx" }

 
sheety_response = requests.post(
    sheety_endpoint, 
    json=sheety_inputs, 
    headers=bearer_headers
)
print(sheety_response.text)

