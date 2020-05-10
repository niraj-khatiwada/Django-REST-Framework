from .serializers import StatusSerializer
from ..models import StatusModel
from rest_framework.response import Response

from rest_framework import permissions, authentication, mixins, generics, pagination
import json

from accounts.rest_api.permisiions import IsOwnerOrReadOnly, BlackListPermission
from .pagination import CustomPagination


class StatusApiView(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = StatusSerializer
    queryset = StatusModel.objects.all()
    search_fields = ('username')

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_serializer_context(self):
        context = {'request': self.request}
        return context


class StatusApiRetrieveView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):
    serializer_class = StatusSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    lookup_field = 'pk'
    queryset = StatusModel.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def get_serializer_context(self):
        context = {'request': self.request}
        return context
