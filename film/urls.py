from django.urls import path

from film.views import FilmListView, FilmDetailView

urlpatterns = [
    path('', FilmListView.as_view()),
    path('<str:id_tayangan>', FilmDetailView.as_view())
]
