from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    path("", views.StatusAPIListView.as_view(), name='status-list-view'),
    path("<int:pk>/", views.StatusAPIRetrieveView.as_view(),
         name='status-retrieve-view'),
    path('jwt-auth/', obtain_jwt_token),
    path('jwt-auth-refresh/', refresh_jwt_token)
]
