from status.rest_api.views import StatusApiView
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework_jwt.settings import api_settings
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .utils import jwt_response_payload_handler
from django.contrib.auth.models import User
from rest_framework import generics, authentication
from .serializers import RegisterSerializer

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_hanlder = jwt_response_payload_handler


class JWTAUTHAPIView(APIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny]

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


class RegisterSerializerView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()

    def get_serializer_context(self):
        return {'request': self.request}


class UserListView(generics.ListAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
    search_fields = ['username']

    def get_serializer_context(self):
        return {'request': self.request}


class UserDetailView(generics.RetrieveAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
    lookup_field = 'pk'

    def get_serializer_context(self):
        return {'request': self.request}
