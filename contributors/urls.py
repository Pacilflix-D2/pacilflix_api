from django.urls import path

from contributors.views import AllContributorsView, AllPemainView, AllScriptWriterView, AllSutradaraView

urlpatterns = [
    path('', AllContributorsView.as_view()),
    path('sutradara/', AllSutradaraView.as_view()),
    path('pemain/', AllPemainView.as_view()),
    path('penulis-skenario/', AllScriptWriterView.as_view())
]
