import requests
import json

BASE_URL = 'http://localhost:8000/'
ENDPOINT = 'api/'


data = {'pk': 9}


def perform_request(method='get'):
    return requests.request(
        method=method, url=BASE_URL + ENDPOINT, data=json.dumps(data), headers={'content-type': 'application/json'})


response = perform_request('get')

print(response.json())
