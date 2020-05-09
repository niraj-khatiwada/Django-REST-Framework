from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings
from .utils import jwt_response_payload_handler


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_hanlder = jwt_response_payload_handler


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={'input_style': 'password'}, write_only=True)
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'token']
        extra_kwargs = {'password': {'write_only': True},
                        'password2': {'write_only': True}}

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.pop('password2')
        if password != password2:
            raise serializers.ValidationError('Passwords do not match')
        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def get_token(self, instance):
        print(self.context['request'].data)
        payload = jwt_payload_handler(instance)
        token_ = jwt_encode_handler(payload)
        return token_
