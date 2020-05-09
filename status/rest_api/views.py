from .serializers import StatusSerializer
from ..models import StatusModel
from rest_framework.response import Response

from rest_framework import permissions, authentication, mixins, generics
import json

from accounts.rest_api.permisiions import IsOwnerOrReadOnly, BlackListPermission
from .pagination import CustomPagination


class StatusApiView(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = StatusSerializer
    search_fields = ('user__username')

    def get_queryset(self):
        q = StatusModel.objects.all()
        if self.request.GET.get('search') is not None:
            q = StatusModel.objects.filter(
                content__icontains=self.request.GET.get('search'))
        return q

    def get(self, request, *args, **kwargs):
        qs = self.get_queryset()
        serialize = StatusSerializer(qs, many=True)
        print("Received HTTP", request.data)
        return Response(serialize.data)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


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
