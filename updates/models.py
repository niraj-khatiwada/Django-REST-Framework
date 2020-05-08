from django.db import models
from django.contrib.auth.models import User
from django.core.serializers import serialize


def upload_image_dir(instance, filename):
    return f'updates/{instance.user}/{filename}'


class Queryset(models.QuerySet):
    def serialize(self):
        print(self.values)
        return serialize(format='json', queryset=self)


class UpdateModelManager(models.Manager):
    def get_queryset(self):
        return Queryset(self.model, using=self._db)


class UpdateModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to=upload_image_dir, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    objects = UpdateModelManager()

    def __str__(self):
        return f'{self.user} - {self.content}' or user

    class Meta:
        db_table = 'update'
        verbose_name = 'Update'

    def serialize(self):
        return serialize(format='json', queryset=[self, ])
