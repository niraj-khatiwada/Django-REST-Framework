from rest_framework.generics import ListAPIView, RetrieveAPIView
from ..models import Status
from .serializers import StatusSerializer

from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin


class StatusAPIListView(CreateModelMixin, ListAPIView):
    serializer_class = StatusSerializer

    def get_queryset(self):
        qs = Status.objects.all()
        return qs

    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class StatusAPIRetrieveView(UpdateModelMixin, DestroyModelMixin, RetrieveAPIView):
    serializer_class = StatusSerializer

    def get_object(self):
        instance = Status.objects.get(pk=self.kwargs.get('pk'))
        return instance

    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
