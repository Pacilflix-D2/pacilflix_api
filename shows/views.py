from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response


class Top10TayanganView(APIView):
    def get(self, request: Request) -> Response:
        ...


class SearchTayanganView(APIView):
    def get(self, request: Request) -> Response:
        ...
