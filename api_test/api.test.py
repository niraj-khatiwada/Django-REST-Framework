import requests
import json

BASE_URL = 'http://localhost:8000/api/'


def perform_request(method="get", data=None, ID='', headers={}):
    data = {}
    # if data is not None:
    #     data = json.dumps(data)
    response = requests.request(
        method=method, url=BASE_URL, headers=headers, data=data)
    return response


data = {
    'user': 1,
    'content': 'Post from request',

}

print(perform_request(method="post", ID=8, data=data,
                      headers={'content-type': 'application/json'}).json())
