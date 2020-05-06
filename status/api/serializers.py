from rest_framework import serializers
from ..models import Status


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['pk', 'user', 'content', 'image']
        read_only_fields = ['user']

    def validate(self, attrs):
        content = attrs.get('content')
        content = None if content == '' else content
        if content is None:
            raise serializers.ValidationError("Content is required")
        return attrs
