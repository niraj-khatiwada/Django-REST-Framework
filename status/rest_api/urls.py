from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('', views.StatusApiView.as_view()),
    path('<int:pk>/', views.StatusApiRetrieveView.as_view(), name='detail'),
]
