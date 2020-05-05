from django.urls import path

from . import views

urlpatterns = [
    path('', views.UpdateModelListAPIView.as_view(), name='list-view'),
    path('<int:pk>/', views.UpdateModelDetailAPIView.as_view(), name='detail-view')
]
