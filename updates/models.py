from django.db import models
from django.conf import settings
from django.shortcuts import reverse


def upload_image(instance, filename):
    return f"=updates/{instance.user}/{filename}"


class UpdateQueryset(models.QuerySet):
    def serialized(self):
        return self


class UpdateManager(models.Manager):
    def get_queryset(self):
        return UpdateQueryset(self.model, using=self._db)


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
