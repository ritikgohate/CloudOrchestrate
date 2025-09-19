import requests
import json

# The API endpoint
url = "http://10.88.0.4:8080/data"

# Open and read the JSON data from the file
with open('/home/g2021wb86154/dev-iot.json', 'r') as file:
    data = json.load(file)

# A POST request to the API
response = requests.post(url, json=data)

# Print the response
print(response.json())