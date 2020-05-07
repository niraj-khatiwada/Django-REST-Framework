from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from . import views

urlpatterns = [
    path('', obtain_jwt_token),
    path('jwt-auth/', views.JWTAuthView.as_view()),
    path('jwt-auth-register', views.JWTAuthRegisterSerializerView.as_view())

]
