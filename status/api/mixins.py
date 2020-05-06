from .serializers import StatusSerializer
from ..models import Status


class StatusAPIRetrieveUpdateDeleteMixins():
    authentication_classes = []
    permission_classes = []
    serializer_class = StatusSerializer
    queryset = Status.objects.all()
    lookup_field = 'pk'
