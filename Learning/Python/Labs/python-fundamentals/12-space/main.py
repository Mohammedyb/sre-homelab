# Exercise: Space Tracker
#
# Fetch live astronaut data from an API and print the names in orbit.
#
# Concepts:
# - API requests
# - JSON parsing
# - Dictionaries
# - Loops

import requests

# Request the current astronaut data from the public API.
response = requests.get("http://api.open-notify.org/astros.json")
json = response.json()

# Display each astronaut currently in space.
print("The people currently in space are: ")
for person in json["people"]:
    print(person["name"])
