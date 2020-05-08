import json
from django.http import JsonResponse, HttpResponse
from .models import UpdateModel
from django.views.generic import DetailView
from django.core.serializers import serialize

import logging
logging.basicConfig(level=logging.DEBUG)


def detail_view(request):
    data = {
        'updates': 1000
    }
    return JsonResponse(data)


class UpdateDetailView(DetailView):
    def get(self, request, *args, **kwargs):
        instance = UpdateModel.objects.get(pk=1).serialize()
        # print("ashjbahjsbjhbas", instance)
        # serialized_data = serialize(
        #     format='json', queryset=[qs, ], fields=('content', 'image'))
        # data = {
        #     'updates': json.loads(serialized_data)
        # }

        qs = UpdateModel.objects.all().serialize()
        logging.info(qs)
        return HttpResponse(qs)
