from django.db import models
from django.contrib.auth.models import User


def image_upload(instance, filename):
    return f'status/{instance.user}/{filename}'


class StatusModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=image_upload, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} {self.content} "or self.user

    class Meta:
        db_table = 'status'
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'
