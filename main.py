import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth
import os


GENDER = "male"
WEIGHT_KG = 75
HEIGHT_CM = 180
AGE = 20
USERNAME="Enter your username"
PASSWORD="Enter your Password"

APP_ID = "Enter Your API ID"
API_KEY ="Enter Your API KEY"
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint="https://api.sheety.co/45bc686177593885061effbfc3e98cb4/kunalWorkoutSheet/workouts"

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
# print(result)

today_date=datetime.now().strftime("%d/%m/%Y")
now_time=datetime.now().strftime("%X")

for exercise in result['exercises']:
    sheet_inputs={
        "workout":{
            "date":today_date,
            "time":now_time,
            "exercise":exercise["name"].title(),
            "duration":exercise["duration_min"],
            "calories":exercise["nf_calories"]
        }       
    }


sheety_header={
    "Authorization":"Basic bnVsbDpudWxs"
}
# sheet_response=requests.post(sheety_endpoint,json=sheet_inputs,headers=headers)
# print(sheet_response.text)

sheet_response = requests.post(
  sheety_endpoint, 
  json=sheet_inputs, 
  auth=(
      "oktim3070", 
      "Kunal@b2001",
  )
)


# sheet_response=requests.post(sheety_endpoint,json=sheet_inputs ,auth=(USERNAME,PASSWORD))
print(sheet_response.text)