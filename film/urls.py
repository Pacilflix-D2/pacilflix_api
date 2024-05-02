from django.urls import path

from film.views import FilmListView, FilmDetailView, FilmUlasanView

urlpatterns = [
    path('', FilmListView.as_view(), name='get-all'),
    path('<str:id_tayangan>/', FilmDetailView.as_view(), name='get-detail'),
    path('<str:id_tayangan>/reviews/',
         FilmUlasanView.as_view(), name='get-reviews')
]
