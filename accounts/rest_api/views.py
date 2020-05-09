from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework_jwt.settings import api_settings
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .utils import jwt_response_payload_handler
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import authentication
from .serializers import RegisterSerializer
from .permisiions import BlackListPermission

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_hanlder = jwt_response_payload_handler


class JWTAUTHAPIView(APIView):
    permission_classes = [BlackListPermission]

    def post(self, request, *args, **kwargs):
        print(request.user)
        if request.user.is_authenticated:
            return Response({"message": "Yoy are already authenticated"})
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            return Response({'error': 'Invalid Credentials'})
        payload = jwt_payload_handler(user)
        token_ = jwt_encode_handler(payload)
        token = jwt_response_payload_hanlder(token=token_, user=user)
        return Response({'token': token})


# class RegisterAPiView(APIView):
#     permission_classes = [permissions.AllowAny]

#     def post(self, request, *args, **kwargs):
#         print(request.user)
#         if request.user.is_authenticated:
#             return Response({"message": "Yoy are already regisetered and authenticated"})
#         email = request.data.get('email')
#         username = request.data.get('username')
#         password = request.data.get('password')
#         password2 = request.data.get('password2')
#         qs = User.objects.filter(username__iexact=username)
#         if qs.exists():
#             return Response({'messgae': 'User already exists'})
#         user = User(username=username, email=email)
#         user.set_password(password)
#         user.save()
#         payload = jwt_payload_handler(user)
#         token_ = jwt_encode_handler(payload)
#         token = jwt_response_payload_hanlder(token=token_, user=user)
#         return Response({'token': token})


class RegisterSerializerView(generics.CreateAPIView):
    permission_classes = [BlackListPermission]
    serializer_class = RegisterSerializer
    queryset = User.objects.all()

    def get_serializer_context(self):
        return {'request': self.request}
