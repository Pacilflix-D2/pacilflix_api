from django.urls import path

from series.views import SeriesListView, SeriesDetailView, SeriesUlasanView, EpisodeDetailView

urlpatterns = [
    path('', SeriesListView.as_view()),
    path('<str:id_tayangan>/', SeriesDetailView.as_view()),
    path('<str:id_tayangan>/reviews/', SeriesUlasanView.as_view()),
    path('<str:id_tayangan>/episodes/<str:sub_judul_eps>/',
         EpisodeDetailView.as_view())
]
