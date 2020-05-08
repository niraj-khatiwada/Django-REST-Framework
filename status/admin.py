from django.contrib import admin
from . import models
from .forms import StatusModelForm


class StatusAdmin(admin.ModelAdmin):
    list_display = ['user', 'content', 'image']

    # class Meta:
    #     model = models.StatusModel

    form = StatusModelForm


admin.site.register(models.StatusModel, StatusAdmin)
