import requests

city = "Richmond, Virginia"
url = "http://api.weatherapi.com/v1/current.json?key=9f8cae5bfba04010820193816260410&q="+city+"=no"
response = requests.get(url)
weather_json = response.json()

temp = weather_json.get("current").get("temp_f")
description = weather_json.get("current").get("condition").get("text")

print("Today's weather in" , city, "is", description, "and", temp, "degrees")
