from typing import Any
from rest_framework.views import APIView
from rest_framework.request import Request
from core.models.film import Film
from core.repositories.film import FilmRepository
from core.utils.response import Response
from rest_framework import status


class FilmListView(APIView):
    def get(self, request: Request) -> Response:
        film_repository = FilmRepository()

        films: list[Film] = film_repository.find_all()

        data_json: list[dict[str, Any]] = []
        for film in films:
            data_json.append(film.to_json())

        return Response(message='Success get films!', data=data_json, status=status.HTTP_200_OK)


class FilmDetailView(APIView):
    def get(self, request: Request, id_tayangan: str) -> Response:
        ...


class FilmUlasanView(APIView):
    def post(self, request: Request, id_tayangan: str) -> Response:
        ...
