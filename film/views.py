from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response


class FilmListView(APIView):
    def get(self, request: Request) -> Response:
        ...


class FilmDetailView(APIView):
    def get(self, request: Request, id_tayangan: str) -> Response:
        ...


class FilmUlasanView(APIView):
    def post(self, request: Request, id_tayangan: str) -> Response:
        ...
