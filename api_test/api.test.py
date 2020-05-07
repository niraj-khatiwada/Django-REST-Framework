import requests
import json


# data = {'pk': 9}


# def perform_request(method='get'):
#     return requests.request(
#         method=method, url=BASE_URL + ENDPOINT, data=data, headers={'content-type': 'application/json'})


# response = perform_request('get')

# print(response.json())


# string = input("Enter a string: ")


# def check_palindrome(string):
#     if string.lower() == string.lower()[::-1]:
#         return "The string is palindrome"
#     else:
#         return "Not a palindrome"
import logging
logging.basicConfig(level=logging.DEBUG)

# print(check_palindrome(string))
BASE_URL = 'http://localhost:8000/'
ENDPOINT = 'api/'
AUTH = 'jwt-auth/'


def send_request(method='get', ID=None, data=None, AUTH=None, token=None):
    token = token if token is not None else {}
    AUTH = AUTH if AUTH is not None else ''
    ID = str(ID) if ID is not None else ''
    data = data if data is not None else {}
    response = requests.request(
        method=method, url=BASE_URL + ENDPOINT + AUTH, headers={'content-type': 'application/json', 'Authorization': 'JWT' + token}, data=json.dumps(data))
    return response


data = {
    'username': 'niraj',
    'password': 'nepal123'
}
token = send_request(method='post', data=data, AUTH=AUTH).json()
logging.info(token)


post_data = {
    'content': 'Fresh content from Request'
}

res = send_request(method='post', data=post_data,
                   token=token.get('token')).json()
logging.debug(res)
