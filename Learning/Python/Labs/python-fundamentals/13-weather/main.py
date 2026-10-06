# Exercise: Weather Lookup
#
# Fetch the current weather for a city and print a summary.
#
# Concepts:
# - API requests
# - JSON parsing
# - Dictionary access
# - Output

import requests

# Build the weather API request and read the result.
city = "Richmond, Virginia"
url = "http://api.weatherapi.com/v1/current.json?key=9f8cae5bfba04010820193816260410&q=" + city + "=no"
response = requests.get(url)
weather_json = response.json()

# Pull the temperature and text description from the JSON response.
temp = weather_json.get("current").get("temp_f")
description = weather_json.get("current").get("condition").get("text")

# Print a simple weather summary to the user.
print("Today's weather in", city, "is", description, "and", temp, "degrees")
