import requests
import json

BASE_URL = 'http://localhost:8000/'
AUTH_ENDPOINT = 'accounts/register/'
API_ENDPOINT = 'api/'


def perform_request(method="get", data=None, ID=None, headers={}, token=None, AUTH_ENDPOINT=''):
    if data is not None:
        data = json.dumps(data)
        headers['Content-Type'] = 'application/json'
    else:
        data = {}
    ID = '' if ID is None else str(ID) + '/'
    if token is not None:
        headers['Authorization'] = "JWT " + token
    response = requests.request(
        method=method, url=BASE_URL + AUTH_ENDPOINT + ID, headers=headers, data=data)
    return response


credentials = {
    'username': 'niraj29',
    'password': 'nepal123',
    'password2': 'nepal123',
    'email': 'niraj29@gmail.com'
}

token = perform_request(method="post", data=credentials,
                        AUTH_ENDPOINT=AUTH_ENDPOINT).json()
print(token)


# data = {
#     'content': 'Post from request 2',
# }

# post_data = perform_request(
#     method="delete", data=data, token=token_key, AUTH_ENDPOINT=API_ENDPOINT, ID=14)

# print(post_data.json())
