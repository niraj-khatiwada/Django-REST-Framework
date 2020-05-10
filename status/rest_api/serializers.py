from rest_framework import serializers
from ..models import StatusModel
from django.contrib.auth.models import User
from django.conf import settings
from rest_framework.reverse import reverse_lazy as api_reverse


class PublicDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class StatusSerializer(serializers.ModelSerializer):
    user = PublicDisplaySerializer(read_only=True)
    detail_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = StatusModel
        fields = ['id', 'user', 'content',
                  'image', 'detail_url']
        read_only_fields = ['user']

    def validate(self, attrs):
        content = attrs.get('content')
        content = None if content == '' else content
        if content is None:
            raise serializers.ValidationError('This field is required')
        return attrs

    def get_detail_url(self, instance):
        return api_reverse(viewname='detail', kwargs={'pk': instance.pk}, request=self.context.get('request'))
