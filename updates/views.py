from django.shortcuts import render
from django.views.generic import ListView
from django.core.serializers import serialize
from django.http import HttpResponse
import json


from .mixins import JSONResonseMixin
from .models import Update
from django.conf import settings

import logging
logging.basicConfig(level=logging.DEBUG)


class UpdateModelDetailView(ListView):
    def get(self, request, *args, **kwargs):
        qs = Update.objects.all().serialized()
        logging.info(qs)
        data = serialize("json", qs)
        return HttpResponse(data, content_type='application/json')
