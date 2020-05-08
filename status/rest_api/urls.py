from django.urls import path
from . import views
urlpatterns = [
    path('', views.StatusApiListView.as_view()),
    path('create/', views.StatuApiCreateView.as_view()),
    path('<int:pk>/', views.StatusApiRetrieveView.as_view()),

]
