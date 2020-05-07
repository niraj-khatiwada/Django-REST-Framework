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
AUTH = 'accounts/jwt-auth/'


def send_request(method='get', ID=None, data=None, AUTH=None, token=None):
    headers = {'Content-Type': 'application/json'}
    if token is not None:
        headers['Authorization'] = 'JWT ' + token
    AUTH = AUTH if AUTH is not None else ''
    ID = (str(ID) + "/") if ID is not None else ''
    data = data if data is not None else {}

    response = requests.request(
        method=method, url=BASE_URL + ENDPOINT + AUTH + ID, headers=headers, data=json.dumps(data))
    return response


data = {
    'username': 'niraj',
    'password': 'nepal123'
}
token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Im5pcmFqIiwiZXhwIjoxNTg4ODczOTM5LCJlbWFpbCI6Im5pcmFqQGdtYWlsLmNvbSIsIm9yaWdfaWF0IjoxNTg4ODczNjM5fQ.PbE_ikcIbtkkUP5h5FvnbeCqORUhf0aW8Ffl4QJX-uI'
token = send_request(method='post', data=data, AUTH=AUTH, token=token).json()
logging.info(token)


# post_data = {
#     'content': 'Fresh updated content from Request'
# }

# res = send_request(method='delete',
#                    token=token.get('token'), ID=12).json()
# logging.debug(res)
