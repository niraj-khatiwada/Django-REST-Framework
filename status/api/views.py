from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveDestroyAPIView, UpdateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from ..models import Status
from rest_framework.response import Response
from .serializers import StatusSerializer
import json

from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin

from .mixins import StatusAPIRetrieveUpdateDeleteMixins

from django.shortcuts import get_object_or_404
from django.http import Http404


class StatusAPIListView(CreateModelMixin, ListAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = StatusSerializer
    queryset = Status.objects.all()

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


# class StatusAPICreateView(CreateAPIView):
#     authentication_classes = []
#     permission_classes = []
#     serializer_class = StatusSerializer


class StatusAPIRetrieveView(UpdateModelMixin, DestroyModelMixin, RetrieveAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = StatusSerializer
    queryset = Status.objects.all()
    lookup_field = 'pk'

    # def get_object(self):
    #     qs = Status.objects.get(id=self.kwargs.get('pk'))
    #     return qs

    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


# class StatusAPIUpdateView(UpdateAPIView):
#     authentication_classes = []
#     permission_classes = []
#     serializer_class = StatusSerializer
#     queryset = Status.objects.all()
#     lookup_field = 'pk'


# class StatusAPIDestroyView(DestroyAPIView):
#     authentication_classes = []
#     permission_classes = []
#     serializer_class = StatusSerializer
#     queryset = Status.objects.all()
#     lookup_field = 'pk'
