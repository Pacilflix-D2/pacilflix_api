from typing import Any
from rest_framework.views import APIView
from rest_framework.request import Request
from core.models.series import Series
from core.models.tayangan import Tayangan
from core.repositories.episode import EpisodeRepository
from core.repositories.series import SeriesRepository
from core.repositories.tayangan import TayanganRepository
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
        series: Series = SeriesRepository().find_by_id(id=id_tayangan)

        tayangan: Tayangan = TayanganRepository().find_by_id(id=series.id_tayangan)
        tayangan_json = tayangan.to_json()
        tayangan_json.pop('id')

        episodes = EpisodeRepository().find_by_id_series(id_series=series.id_tayangan)
        episode_list_json: list[dict[str, Any]] = []
        for episode in episodes:
            episode_list_json.append(episode.to_json())

        series_json = {**series.to_json(), **tayangan_json,
                       "episodes": episode_list_json}

        return Response(message='Success get series detail!', data=series_json, status=status.HTTP_200_OK)


class SeriesUlasanView(APIView):
    def post(self, request: Request, id_tayangan: str) -> Response:
        ...
