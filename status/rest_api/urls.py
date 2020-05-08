from django.urls import path
from . import views
urlpatterns = [
    path('', views.StatusApiView.as_view()),
    path('<int:pk>/', views.StatusApiRetrieveView.as_view())
]
