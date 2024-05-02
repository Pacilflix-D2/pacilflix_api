from django.urls import path

from downloads.views import DownloadListView

urlpatterns = [
    path('', DownloadListView.as_view())
]
