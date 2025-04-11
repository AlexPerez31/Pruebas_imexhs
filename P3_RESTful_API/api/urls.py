from django.urls import path
from .views.data_upload_view import DataUploadView
from .views.data_retrieve_view import DataListView, DataDetailView
from .views.data_update_view import DataUpdateView
from .views.data_delete_view import DataDeleteView

urlpatterns = [
    path("data/upload/", DataUploadView.as_view(), name="data-upload"),
    path("data/", DataListView.as_view(), name="data-read"),
    path("data/<str:pk>/", DataDetailView.as_view(), name="data-detail"),
    path("data/update/<str:pk>/", DataUpdateView.as_view(), name="data-update"),
    path("data/delete/<str:pk>/", DataDeleteView.as_view(), name="data-delete"),
]