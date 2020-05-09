from django.urls import path
from . import views
urlpatterns = [
    path('obtain-jwt-auth/', views.JWTAUTHAPIView.as_view())
]
