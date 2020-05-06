from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveDestroyAPIView, UpdateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from ..models import Status
from rest_framework.response import Response
from .serializers import StatusSerializer
import json

from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin

from .mixins import StatusAPIRetrieveUpdateDeleteMixins

from django.shortcuts import get_object_or_404
from django.http import Http404


class StatusAPIListView(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, ListAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = StatusSerializer

    def get_queryset(self):
        qs = Status.objects.all()
        search = self.request.GET.get('q')
        if search:
            qs = Status.objects.filter(content__icontains=search)
        return qs

    def get_object(self):
        pk = self.request.GET.get('pk')
        try:
            obj = get_object_or_404(Status, pk=pk)
        except:
            raise Http404
        return obj

    def get(self, request, *args, **kwargs):
        passed_id = self.request.GET.get('pk')
        obj = self.get_object() if passed_id else None
        if obj is not None:
            return self.retrieve(request, *args, **kwargs)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        passed_id = self.request.GET.get('pk')
        instance = self.get_object() if passed_id else None
        if instance is not None:
            return self.update(request, *args, **kwargs)
        return super().create(request, *args, **kwargs)


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

#     def put(self, request, *args, **kwargs):
#         return super().update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)


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
