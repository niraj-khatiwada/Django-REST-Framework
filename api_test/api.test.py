import requests
import json

BASE_URL = 'http://localhost:8000/api/'
AUTH_ENDPOINT = 'obtain-jwt-auth/'


def perform_request(method="get", data=None, ID='', headers={}, token=None, AUTH_ENDPOINT=''):
    # if data is not None:
    #     data = json.dumps(data)
    #     headers['Content-Type'] = 'application/json'
    # else:
    #     data = {}
    if token is not None:
        headers['Authorization'] = "JWT " + token
        print("headers", headers)
    response = requests.request(
        method=method, url=BASE_URL + AUTH_ENDPOINT, headers=headers, data=data)
    return response


credentials = {
    'username': 'niraj',
    'password': 'nepal123'
}

token = perform_request(method="post", data=credentials,
                        AUTH_ENDPOINT=AUTH_ENDPOINT).json()
print(token)


data = {
    'content': 'Post from request',
}

post_data = perform_request(
    method="post", data=data, token=token['token'])

print(post_data.json())
