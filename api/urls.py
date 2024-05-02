from django.urls import include, path

urlpatterns = [
    path('auth/', include(('authentication.urls', 'auth'))),
    path('contributors/', include(('contributors.urls', 'contributors'))),
    path('downloads/', include(('downloads.urls', 'downloads'))),
    path('shows/', include(('shows.urls', 'shows'))),
    path('favorites/', include(('favorites.urls', 'favorites'))),
    path('subcriptions/', include(('subcriptions.urls', 'subcriptions'))),
]
