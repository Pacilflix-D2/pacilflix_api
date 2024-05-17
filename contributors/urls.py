from django.urls import path

from contributors.views import ContributorsView

urlpatterns = [
    path('', ContributorsView.as_view()),
]
