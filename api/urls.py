from django.urls import include, path

urlpatterns = [
    path('auth/', include(('authentication.urls', 'auth'))),
    path('contributors/', include(('contributors.urls', 'contributors'))),
    path('downloads/', include(('downloads.urls', 'downloads'))),
    path('shows/', include(('shows.urls', 'shows'))),
    path('favorites/', include(('favorites.urls', 'favorites'))),
    path('subscriptions/', include(('subscriptions.urls', 'subscriptions'))),
    path('film/', include(('film.urls', 'film'))),
    path('series/', include(('series.urls', 'series'))),
]
