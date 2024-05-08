from django.urls import path

from favorites.views import FavoriteListView, FavoriteListDetailView

urlpatterns = [
    path('', FavoriteListView.as_view()),
    path('detail/', FavoriteListDetailView.as_view())
]
