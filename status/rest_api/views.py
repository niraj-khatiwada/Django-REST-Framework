from .serializers import StatusSerializer
from ..models import StatusModel
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins

from rest_framework import permissions
from rest_framework import authentication
import json


class StatusApiView(mixins.CreateModelMixin, generics.ListAPIView):
    # authentication_classes = [authentication.SessionAuthentication]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = StatusSerializer

    def get_queryset(self):
        q = StatusModel.objects.all()
        if self.request.GET.get('search') is not None:
            q = StatusModel.objects.filter(
                content__icontains=self.request.GET.get('search'))
        return q

    def get(self, request, *args, **kwargs):
        qs = self.get_queryset()
        print("ashjbajsb", qs)
        serialize = StatusSerializer(qs, many=True)
        return Response(serialize.data)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StatusApiRetrieveView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):
    # authentication_classes = [authentication.SessionAuthentication]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = StatusSerializer

    def get_object(self):
        pk = self.kwargs.get('pk')
        return StatusModel.objects.get(pk=pk)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
