from django.urls import path
from .views import SearchTayanganView, Top10TayanganView, Top10TayanganCountryView

urlpatterns = [
    path('top-10/', Top10TayanganView.as_view()),
    path('top-10/country/', Top10TayanganCountryView.as_view()),
    path('search/', SearchTayanganView.as_view()),
]
