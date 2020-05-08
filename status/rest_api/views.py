from .serializers import StatusSerializer
from ..models import StatusModel

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView


class StatusApiListView(ListAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = StatusSerializer
    queryset = StatusModel.objects.all()


class StatusApiRetrieveView(RetrieveAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = StatusSerializer

    def get_object(self):
        return StatusModel.objects.first()


class StatuApiCreateView(CreateAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = StatusSerializer
    queryset = StatusModel.objects.all()
