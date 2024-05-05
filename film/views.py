from typing import Any
from rest_framework.views import APIView
from rest_framework.request import Request
from core.models.film import Film
from core.models.ulasan import Ulasan
from core.repositories.film import FilmRepository
from core.repositories.ulasan import UlasanRepository
from core.utils.exceptions.not_found import NotFoundException
from core.utils.response import Response
from rest_framework import status


class FilmListView(APIView):
    def get(self, request: Request) -> Response:
        film_repository = FilmRepository()
        # print('hi')

        films: list[Film] = film_repository.find_all()
        # print('FILMS')
        # print(films)

        data_json: list[dict[str, Any]] = []
        for film in films:
            data_json.append(film.to_json())

        return Response(message='Success get films!', data=data_json, status=status.HTTP_200_OK)


class FilmDetailView(APIView):
    def get(self, request: Request, id_tayangan: str) -> Response:
        film_repository = FilmRepository()

        film = film_repository.find_by_id(id_tayangan=id_tayangan)

        data_json = {
            'film': film.to_json()
        }

        return Response(message='Success get film details!', data=data_json, status=status.HTTP_200_OK)


class FilmUlasanView(APIView):
    def get(self, request: Request, id_tayangan: str) -> Response:
        film_repository = FilmRepository()
        film: Film = film_repository.find_by_id(id_tayangan=id_tayangan)

        print('uwu')
        ulasan_repository = UlasanRepository()
        reviews: list[Ulasan] = ulasan_repository.find_by_id_tayangan(
            id_tayangan=film.id_tayangan)

        data_json: list[dict[str, Any]] = []
        for review in reviews:
            data_json.append(review.to_json())

        return Response(message='Success get film reviews!', data=data_json, status=status.HTTP_200_OK)

    def post(self, request: Request, id_tayangan: str) -> Response:
        film_repository = FilmRepository()
        film: Film = film_repository.find_by_id(id_tayangan=id_tayangan)
