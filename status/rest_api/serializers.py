from rest_framework import serializers
from ..models import StatusModel


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusModel
        fields = ['id','user', 'content', 'image']

    def validate(self, attrs):
        content = attrs.get('content')
        content = None if content == '' else content
        if content is None:
            raise serializers.ValidationError('This field is required')
        return attrs
