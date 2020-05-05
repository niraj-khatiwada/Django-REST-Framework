from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.core.serializers import serialize


def upload_image(instance, filename):
    return f"=updates/{instance.user}/{filename}"


class UpdateQuerySet(models.QuerySet):
    def serialized(self, instance):
        if instance is not None:
            qs = self.get(id=instance.id)
            return serialize("json", [qs, ])
        else:
            qs = self
            return serialize("json", qs)


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
