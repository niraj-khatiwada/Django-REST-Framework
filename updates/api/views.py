from ..models import Update
from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import Http404

import logging
logging.basicConfig(level=logging.DEBUG)
# Detail, Update, Delete


class UpdateModelDetailAPIView(View):
    def get(self, request, *args, **kwargs):
        try:
            instance = get_object_or_404(
                Update, pk=self.kwargs.get("pk"))
        except Update.DoesNotExist:
            raise Http404
        json_data = Update.objects.get_serialized_data(instance)
        return HttpResponse(json_data, content_type='application/json')

    def put(self, request, *args, **kwargs):
        pass

    def delete(self, request, *args, **kwargs):
        pass


# List, Create
class UpdateModelListAPIView(View):
    def get(self, request, *args, **kwargs):
        try:
            obj = get_list_or_404(Update, pk=1)
        except:
            raise Http404
        json_data = Update.objects.get_serialized_data()
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        pass
