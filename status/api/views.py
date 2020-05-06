from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveDestroyAPIView, UpdateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from ..models import Status
from rest_framework.response import Response
from .serializers import StatusSerializer
import json

from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin

from .mixins import StatusAPIRetrieveUpdateDeleteMixins


class StatusAPIListView(CreateModelMixin, ListAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = StatusSerializer

    def get_queryset(self):
        qs = Status.objects.all()
        search = self.request.GET.get('q')
        if search:
            qs = Status.objects.filter(content__icontains=search)
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


# class StatusAPICreateView(CreateAPIView):
#     authentication_classes = []
#     permission_classes = []
#     serializer_class = StatusSerializer


# class StatusAPIRetrieveView(UpdateModelMixin, DestroyModelMixin, RetrieveAPIView):
#     authentication_classes = []
#     permission_classes = []
#     serializer_class = StatusSerializer
#     queryset = Status.objects.all()
#     lookup_field = 'pk'

#     # def get_object(self):
#     #     qs = Status.objects.get(id=self.kwargs.get('pk'))
#     #     return qs


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
