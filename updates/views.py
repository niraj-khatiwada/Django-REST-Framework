from django.shortcuts import render
from django.views.generic import *
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
        instance = Update.objects.get(id=1)
        json_data = Update.objects.get_serialized_data(instance)
        return HttpResponse(json_data, content_type='application/json')


class UpdateModelListView(ListView):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.all()
        json_data = Update.objects.get_serialized_data()
        return HttpResponse(json_data, content_type='application/json')
