from datetime import timedelta
from typing import Any
from rest_framework.views import APIView
from rest_framework.request import Request
from core.models.riwayat_nonton import RiwayatNonton
from core.models.tayangan import Tayangan
from core.repositories.riwayat_nonton import RiwayatNontonRepository
from core.repositories.tayangan import TayanganRepository
from core.utils.response import Response
from rest_framework import status


class Top10TayanganView(APIView):
    def get(self, request: Request) -> Response:
        tayangan_repository = TayanganRepository()
        riwayat_nonton_repository = RiwayatNontonRepository()

        shows: list[Tayangan] = tayangan_repository.find_all()

        for show in shows:
            watch_histories: list[RiwayatNonton] = riwayat_nonton_repository.find_by_id_tayangan_last_week(
                id_tayangan=show.id)

            for watch_history in watch_histories:
                watch_time: timedelta = watch_history.end_date_time - watch_history.start_date_time

                # lanjut bentar, seharusnya ini ngukur lama nonton dengan durasi full tayangannya, kalau lebih dari 70%, nambah 1 views
                # if watch_time > timedelta

        data_json: list[dict[str, Any]] = []
        for show in shows:
            data_json.append(show.to_json())

        return Response(message='Success get top 10 shows!', data=data_json, status=status.HTTP_200_OK)


class SearchTayanganView(APIView):
    def get(self, request: Request) -> Response:
        ...
