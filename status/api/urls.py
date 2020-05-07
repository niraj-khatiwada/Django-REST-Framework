from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.StatusAPIListView.as_view(), name='status-list-view'),
    path("<int:pk>/", views.StatusAPIRetrieveView.as_view(),
         name='status-retrieve-view'),
    path('accounts/', include('accounts.rest_framework.urls'))
]
