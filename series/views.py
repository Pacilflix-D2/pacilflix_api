from datetime import datetime
from typing import Any
from rest_framework.views import APIView
from rest_framework.request import Request
from core.models.contributor import Contributor
from core.models.episode import Episode
from core.models.pengguna import Pengguna
from core.models.series import Series
from core.models.tayangan import Tayangan
from core.models.ulasan import Ulasan
from core.repositories.contributors import ContributorRepository
from core.repositories.episode import EpisodeRepository
from core.repositories.gender import GenreRepository
from core.repositories.pemain import PemainRepository
from core.repositories.penulis_skenario import PenulisSkenarioRepository
from core.repositories.series import SeriesRepository
from core.repositories.tayangan import TayanganRepository
from core.repositories.ulasan import UlasanRepository
from core.utils.exceptions.bad_request import BadRequestException
from core.utils.exceptions.unauthorized import UnauthorizedException
from core.utils.get_user import get_user
from core.utils.response import Response
from rest_framework import status


class SeriesListView(APIView):
    def get(self, request: Request) -> Response:
        series_list: list[Series] = SeriesRepository().find_all()

        data_json: list[dict[str, Any]] = []
        for series in series_list:
            tayangan: Tayangan = TayanganRepository().find_by_id(id=series.id_tayangan)
            tayangan_json = tayangan.to_json()
            tayangan_json.pop('id')

            series_json = {**series.to_json(), **tayangan_json}

            data_json.append(
                series_json
            )

        return Response(message='Success get series list!', data=data_json, status=status.HTTP_200_OK)


class SeriesDetailView(APIView):
    def get(self, request: Request, id_tayangan: str) -> Response:
        user: Pengguna | None = get_user(request=request)

        if not user:
            raise UnauthorizedException('Must login first.')

        series: Series = SeriesRepository().find_by_id(id=id_tayangan)

        tayangan: Tayangan = TayanganRepository().find_by_id(id=series.id_tayangan)
        tayangan_json = tayangan.to_json()
        tayangan_json.pop('id')
        tayangan_json.pop('id_sutradara')

        episodes = EpisodeRepository().find_by_id_series(id_series=series.id_tayangan)

        genres = GenreRepository().find_by_id_tayangan(id_tayangan=tayangan.id)

        sutradara: Contributor = ContributorRepository().find_by_id(id=tayangan.id_sutradara)

        players = PemainRepository().find_by_id_tayangan(id_tayangan=tayangan.id)

        writers = PenulisSkenarioRepository().find_by_id_tayangan(id_tayangan=tayangan.id)

        series_json = {
            **series.to_json(),
            **tayangan_json,
            "total_views": tayangan.get_total_views(),
            "rating_avg": tayangan.get_rating(),
            "episodes": [episode.to_json() for episode in episodes],
            "sutradara": {
                **sutradara.to_json()
            },
            "genres": [genre.to_json() for genre in genres],
            "players": [player.to_json() for player in players],
            "writers": [writer.to_json() for writer in writers]
        }

        return Response(message='Success get series detail!', data=series_json, status=status.HTTP_200_OK)


class SeriesUlasanView(APIView):
    def get(self, request: Request, id_tayangan: str) -> Response:
        user: Pengguna | None = get_user(request=request)

        if not user:
            raise UnauthorizedException('Must login first.')

        tayangan: Tayangan = TayanganRepository().find_by_id(id=id_tayangan)

        reviews: list[Ulasan] = UlasanRepository(
        ).find_by_id_tayangan(id_tayangan=tayangan.id)

        data_json: list[dict[str, Any]] = []
        for review in reviews:
            data_json.append(review.to_json())

        return Response(message='Success get reviews!', data=data_json, status=status.HTTP_200_OK)

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


class EpisodeDetailView(APIView):
    def get(self, request: Request, id_tayangan: str, sub_judul_eps: str) -> Response:
        user: Pengguna | None = get_user(request=request)

        if not user:
            raise UnauthorizedException('Must login first.')

        episode: Episode = EpisodeRepository().find_by_pk(
            id_series=id_tayangan, sub_judul=sub_judul_eps)

        return Response(message='Success get episode detail!', data=episode.to_json(), status=status.HTTP_200_OK)
