from datetime import datetime
from typing import Any
from rest_framework.views import APIView
from rest_framework.request import Request
from core.models.contributor import Contributor
from core.models.film import Film
from core.models.pengguna import Pengguna
from core.models.tayangan import Tayangan
from core.models.ulasan import Ulasan
from core.repositories.contributors import ContributorRepository
from core.repositories.film import FilmRepository
from core.repositories.gender import GenreRepository
from core.repositories.pemain import PemainRepository
from core.repositories.penulis_skenario import PenulisSkenarioRepository
from core.repositories.tayangan import TayanganRepository
from core.repositories.ulasan import UlasanRepository
from core.utils.exceptions.bad_request import BadRequestException
from core.utils.exceptions.unauthorized import UnauthorizedException
from core.utils.get_user import get_user
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
            tayangan = TayanganRepository().find_by_id(id=film.id_tayangan)
            data_json.append({**film.to_json(), **tayangan.to_json()})

        return Response(message='Success get films!', data=data_json, status=status.HTTP_200_OK)


class FilmDetailView(APIView):
    def get(self, request: Request, id_tayangan: str) -> Response:
        film_repository = FilmRepository()

        film = film_repository.find_by_id(id_tayangan=id_tayangan)

        tayangan: Tayangan = TayanganRepository().find_by_id(id=film.id_tayangan)
        tayangan_json = tayangan.to_json()
        tayangan_json.pop('id')
        tayangan_json.pop('id_sutradara')

        genres = GenreRepository().find_by_id_tayangan(id_tayangan=tayangan.id)

        sutradara: Contributor = ContributorRepository().find_by_id(id=tayangan.id_sutradara)

        players = PemainRepository().find_by_id_tayangan(id_tayangan=tayangan.id)

        writers = PenulisSkenarioRepository().find_by_id_tayangan(id_tayangan=tayangan.id)

        data_json = {
            **film.to_json(),
            **tayangan_json,
            "total_views": tayangan.get_total_views_last_week(),
            "rating_avg": tayangan.get_rating(),
            "sutradara": sutradara.to_json(),
            "genres": [genre.to_json() for genre in genres],
            "players": [player.to_json() for player in players],
            "writers": [writer.to_json() for writer in writers],
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
        user: Pengguna | None = get_user(request=request)

        if not user:
            raise UnauthorizedException('Must login first.')

        deskripsi: str | None = request.data.get('deskripsi', None)
        rating: int = request.data.get('rating', 0)

        if deskripsi and len(deskripsi) > 255:
            raise BadRequestException(
                'Maximum length for deskripsi is 255 characters.')

        tayangan: Tayangan = TayanganRepository().find_by_id(id=id_tayangan)

        UlasanRepository().create(id_tayangan=tayangan.id, username=user.username,
                                  timestamp=datetime.now(), rating=rating, deskripsi=deskripsi)

        data_json: list[dict[str, Any]] = []
        for ulasan in UlasanRepository().find_by_id_tayangan(id_tayangan=tayangan.id):
            data_json.append(ulasan.to_json())

        return Response(message='Success send ulasan!', data=data_json, status=status.HTTP_201_CREATED)
