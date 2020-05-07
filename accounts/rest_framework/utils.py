def jwt_response_payload_hanlder(token, user=None, request=None):
    return {
        'token': token,
        'user': user.username
    }
