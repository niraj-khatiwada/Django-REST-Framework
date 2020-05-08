from rest_framework import serializers
from ..models import StatusModel


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusModel
        fields = ['user', 'content', 'image']
