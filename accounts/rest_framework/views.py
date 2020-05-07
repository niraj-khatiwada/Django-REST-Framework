from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login
from rest_framework_jwt.settings import api_settings
from rest_framework.generics import CreateAPIView
from .serializers import JWTAuthSerialier

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_hanlder = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER


class JWTAuthView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return Response({'error': 'Already logged in'})
        username = self.request.data.get('username')
        password = self.request.data.get('password')
        user = authenticate(username=username, password=password)
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        response = jwt_response_payload_hanlder(token, user)
        return Response(response)


class JWTAuthRegisterSerializerView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = JWTAuthSerialier
