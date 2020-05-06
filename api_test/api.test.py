import requests

BASE_URL = 'http://localhost:8000/'
ENDPOINT = 'api/'

response = requests.get(BASE_URL + ENDPOINT)
json_data = response.json()
print(type(json_data))
