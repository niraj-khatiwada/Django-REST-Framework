from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveDestroyAPIView, UpdateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from ..models import Status
from rest_framework.response import Response
from .serializers import StatusSerializer
import json

from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin

from .mixins import StatusAPIRetrieveUpdateDeleteMixins

from django.shortcuts import get_object_or_404
from django.http import Http404


def is_json(json_data):
    try:
        real_json = json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid


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
        pk = self.request.GET.get('pk') or self.passed_id
        try:
            obj = get_object_or_404(self.queryset(), pk=pk)
        except:
            raise Http404
        return obj

    def get(self, request, *args, **kwargs):
        url_passed_id = self.request.GET.get('pk')
        json_data = {}
        body_ = self.request.body
        if is_json(body_):
            json_data = json.loads(body_)
        new_passed_id = json_data.get('pk', None)
        passed_id = url_passed_id or new_passed_id or None
        self.passed_id = new_passed_id
        if passed_id is not None:
            return self.retrieve(request, *args, **kwargs)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
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
