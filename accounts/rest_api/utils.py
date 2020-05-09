from django.conf import settings
import datetime


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': user.username,
        'expires in': datetime.datetime.now() + settings.JWT_AUTH['JWT_EXPIRATION_DELTA']
    }
