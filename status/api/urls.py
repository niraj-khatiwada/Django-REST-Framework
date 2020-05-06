from django.urls import path
from . import views

urlpatterns = [
    path("", views.StatusAPIListView.as_view(), name='status-list-view'),
    path("<int:pk>/", views.StatusAPIRetrieveView.as_view(),
         name='status-retrieve-view'),
]
