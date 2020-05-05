from ..models import Update
from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import Http404

import logging
logging.basicConfig(level=logging.DEBUG)
# Detail, Update, Delete


class UpdateModelDetailAPIView(View):
    def get(self, request, *args, **kwargs):
        instance = Update.objects.get(id=self.kwargs.get("pk"))
        logging.info(instance)
        if instance:
            json_data = Update.objects.get_serialized_data(instance)
            return HttpResponse(json_data, content_type='application/json')
        raise Http404

    def put(self, request, *args, **kwargs):
        pass

    def delete(self, request, *args, **kwargs):
        pass


# List, Create
class UpdateModelListAPIView(View):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.all()
        json_data = Update.objects.get_serialized_data()
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        pass
