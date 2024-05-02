from django.urls import path

from series.views import SeriesListView, SeriesDetailView

urlpatterns = [
    path('', SeriesListView.as_view()),
    path('<str:id_tayangan>', SeriesDetailView.as_view())
]
