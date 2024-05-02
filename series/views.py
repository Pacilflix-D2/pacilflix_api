from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response


class SeriesListView(APIView):
    def get(self, request: Request) -> Response:
        ...


class SeriesDetailView(APIView):
    def get(self, request: Request, id_tayangan: str) -> Response:
        ...
