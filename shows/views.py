from typing import Any
from rest_framework.views import APIView
from rest_framework.request import Request
from core.models.tayangan import Tayangan
from core.repositories.tayangan import TayanganRepository
from core.utils.response import Response
from rest_framework import status


class Top10TayanganView(APIView):
    def get(self, request: Request) -> Response:
        tayangan_repository = TayanganRepository()
        print('hilih')

        shows: list[Tayangan] = tayangan_repository.find_all()

        for show in shows:
            print('hi')
            print(show.get_total_views_last_week())

        data_json: list[dict[str, Any]] = []
        for show in shows:
            data_json.append(show.to_json())

        return Response(message='Success get top 10 shows!', data=data_json, status=status.HTTP_200_OK)


class SearchTayanganView(APIView):
    def get(self, request: Request) -> Response:
        ...
