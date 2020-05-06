from django.urls import path
from .views import StatusAPIListView

urlpatterns = [
    path("list/", StatusAPIListView.as_view(), name='status-list-view')
]
