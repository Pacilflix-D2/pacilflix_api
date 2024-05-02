from django.urls import path
from .views import SearchTayanganView, Top10TayanganView

urlpatterns = [
    path('top-10/', Top10TayanganView.as_view()),
    path('search/', SearchTayanganView.as_view()),
]
