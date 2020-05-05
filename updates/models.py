from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.core.serializers import serialize
import json


def upload_image(instance, filename):
    return f"=updates/{instance.user}/{filename}"


def returnPythonDict(json_data):
    all_array = json.loads(json_data)
    python_dict = [x.get('fields') for x in all_array]
    return json.dumps(python_dict)


class UpdateQuerySet(models.QuerySet):
    def serialized(self, instance):
        if instance is not None:
            qs = self.get(id=instance.id)
            json_data = serialize("json", [qs, ],)
            return returnPythonDict(json_data)
        else:
            json_data = serialize("json", self)
            return returnPythonDict(json_data)


class UpdateManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return UpdateQuerySet(self.model, using=self._db)

    def get_serialized_data(self, instance=None):
        return self.get_queryset().serialized(instance)


class Update(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_image, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(
        auto_now=True, verbose_name='Last Updated')

    objects = UpdateManager()

    def __str__(self):
        return f'{self.user}-{self.content}' or self.user
