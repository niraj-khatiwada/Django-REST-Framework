from django.db import models


class StatusQuerySet(models.QuerySet):
    pass


class StatusManager(models.Manager):
    def get_queryset(self):
        return StatusQuerySet(self.model, using=self._db)


def upload_image_to(instance, filename):
    return f'status/{instance.user}/{filename}'


class Status(models.Model):
    user = models.ForeignKey()
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_image_to, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    objects = StatusManager()

    def __str__(self):
        return self.user + self.content
