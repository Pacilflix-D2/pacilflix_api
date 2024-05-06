from datetime import datetime
from typing import Any
from rest_framework.views import APIView
from rest_framework.request import Request
from core.models.contributor import Contributor
from core.models.pengguna import Pengguna
from core.models.series import Series
from core.models.tayangan import Tayangan
from core.repositories.contributors import ContributorRepository
from core.repositories.episode import EpisodeRepository
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
    '''
    TODO:
    - belum ada x di response nya:
        - genre
        - pemain
        - penulis skenario

    '''

    def get(self, request: Request, id_tayangan: str) -> Response:
        series: Series = SeriesRepository().find_by_id(id=id_tayangan)

        tayangan: Tayangan = TayanganRepository().find_by_id(id=series.id_tayangan)
        tayangan_json = tayangan.to_json()
        tayangan_json.pop('id')
        tayangan_json.pop('id_sutradara')

        episodes = EpisodeRepository().find_by_id_series(id_series=series.id_tayangan)
        episode_list_json: list[dict[str, Any]] = []
        for episode in episodes:
            episode_list_json.append(episode.to_json())

        sutradara: Contributor = ContributorRepository().find_by_id(id=tayangan.id_sutradara)

        series_json = {
            **series.to_json(),
            **tayangan_json,
            "episodes": episode_list_json,
            "sutradara": {
                **sutradara.to_json()
            }
        }

        return Response(message='Success get series detail!', data=series_json, status=status.HTTP_200_OK)


class SeriesUlasanView(APIView):
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
