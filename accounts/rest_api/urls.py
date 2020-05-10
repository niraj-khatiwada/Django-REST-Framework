from django.urls import path
from . import views
urlpatterns = [
    path('obtain-jwt-auth/', views.JWTAUTHAPIView.as_view()),
    path('register/', views.RegisterSerializerView.as_view()),
    path('list', views.UserListView.as_view()),
    path('detail/<int:pk>/', views.UserDetailView.as_view()),
]
