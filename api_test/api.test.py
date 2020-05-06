import requests

BASE_URL = 'http://localhost:8000/'
ENDPOINT = 'api/'
ID = 9
a = {'pk': ID}


def perform_request(ID, method='get'):
    return requests.request(
        method=method, url=BASE_URL + ENDPOINT, params=a, data=a)


response = perform_request(9, 'get')
print(response.json())
