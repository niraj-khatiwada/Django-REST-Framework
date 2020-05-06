from rest_framework.generics import ListAPIView
from ..models import Status
from rest_framework.response import Response
from .serializers import StatusSerializer
import json


class StatusAPIListView(ListAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = StatusSerializer

    # def get(self, request, *args, **kwargs):
    #     qs = Status.objects.all()
    #     serializer = StatusSerializer(qs, many=True)
    #     return Response(serializer.data)

    def get_queryset(self):
        qs = Status.objects.all()
        search = self.request.GET.get('q')
        if search:
            qs = Status.objects.filter(content__icontains=search)
        return qs
