from django.urls import path
from . import views

urlpatterns = [
    path("", views.StatusAPIListView.as_view(), name='status-list-view'),
    # path("create/", views.StatusAPICreateView.as_view(), name='status-create-view'),
    path("<int:pk>/", views.StatusAPIRetrieveView.as_view(),
         name='status-retrieve-view'),
    # path("update/<int:pk>/", views.StatusAPIUpdateView.as_view(),
    #      name='status-update-view'),
    # path("delete/<int:pk>/", views.StatusAPIDestroyView.as_view(),
    #      name='status-delete-view'),
]
