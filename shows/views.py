from typing import Any
from rest_framework.views import APIView
from rest_framework.request import Request
from core.models.pengguna import Pengguna
from core.models.tayangan import Tayangan
from core.repositories.tayangan import TayanganRepository
from core.utils.exceptions.unauthorized import UnauthorizedException
from core.utils.get_user import get_user
from core.utils.response import Response
from rest_framework import status

from shows.services import get_top_10_from_tayangan_array


class Top10TayanganView(APIView):
    def get(self, request: Request) -> Response:
        tayangan_repository = TayanganRepository()
        print('hilih')

        shows: list[Tayangan] = tayangan_repository.find_all()

        top_10_shows = get_top_10_from_tayangan_array(shows=shows)

        data_json: list[dict[str, Any]] = []
        for show in top_10_shows:
            data_json.append(
                {
                    **show.to_json(),
                    "total_views": show.get_total_views_last_week(),
                    "type": show.get_type()
                }
            )

        return Response(message='Success get top 10 shows!', data=data_json, status=status.HTTP_200_OK)


class Top10TayanganCountryView(APIView):
    def get(self, request: Request) -> Response:
        user: Pengguna | None = get_user(request=request)

        if not user:
            raise UnauthorizedException('Must login first.')

        shows: list[Tayangan] = TayanganRepository().find_top_tayangan_from_user_country(
            country=user.negara_asal)

        top_10_shows: list[Tayangan] = get_top_10_from_tayangan_array(
            shows=shows)

        data_json: list[dict[str, Any]] = []
        for show in top_10_shows:
            data_json.append(
                {
                    **show.to_json(),
                    "total_views": show.get_total_views_last_week(),
                    "type": show.get_type()
                }
            )

        return Response(message='Success get top 10 shows!', data=data_json, status=status.HTTP_200_OK)


class SearchTayanganView(APIView):
    def get(self, request: Request) -> Response:
        search: str | None = request.query_params.get('search')

        if search:
            shows = TayanganRepository().find_by_judul(judul=search)
        else:
            shows = TayanganRepository().find_all()

        data_json = [
            {
                **show.to_json(),
                "type": show.get_type()
            } for show in shows
        ]

        return Response(message='Success search shows by judul!', data=data_json)
