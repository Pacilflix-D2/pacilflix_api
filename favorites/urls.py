from django.urls import path

from favorites.views import FavoriteListView

urlpatterns = [
    path('', FavoriteListView.as_view())
]
