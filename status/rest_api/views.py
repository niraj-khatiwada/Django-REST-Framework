from .serializers import StatusSerializer
from ..models import StatusModel
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins

from rest_framework import permissions
from rest_framework import authentication
import json

from accounts.rest_api.permisiions import IsOwnerOrReadOnly, BlackListPermission


class StatusApiView(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = StatusSerializer

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
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = 'pk'
    queryset = StatusModel.objects.all()
    # def get_object(self):
    #     pk = self.kwargs.get('pk')
    #     return StatusModel.objects.get(pk=pk)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
