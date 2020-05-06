import requests

BASE_URL = 'http://localhost:8000/'
ENDPOINT = 'api/'
ID = 7
response = requests.get(BASE_URL + ENDPOINT + str(ID))

print(response.json())
