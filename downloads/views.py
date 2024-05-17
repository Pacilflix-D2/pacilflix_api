from datetime import datetime
from rest_framework.views import APIView
from rest_framework.request import Request
from core.models.pengguna import Pengguna
from core.repositories.tayangan_terunduh import TayanganTerunduhRepository
from core.utils.exceptions.bad_request import BadRequestException
from core.utils.exceptions.unauthorized import UnauthorizedException
from core.utils.get_user import get_user
from core.utils.response import Response
from rest_framework import status

from downloads.services import get_all_tayangan_by_username_json


class DownloadListView(APIView):
    def get(self, request: Request) -> Response:
        user: Pengguna | None = get_user(request=request)

        if not user:
            raise UnauthorizedException('Must login to access downloads.')

        data_json = get_all_tayangan_by_username_json(username=user.username)

        return Response(message='Success get downloads!', data=data_json, status=status.HTTP_200_OK)

    def delete(self, request: Request) -> Response:
        user: Pengguna | None = get_user(request=request)

        if not user:
            raise UnauthorizedException('Must login to access downloads.')

        timestamp: str | None = request.data.get('timestamp', None)
        if not timestamp:
            raise BadRequestException('Timetamp is required.')
        datetime_timestamp: datetime = datetime.strptime(
            timestamp, '%Y-%m-%dT%H:%M:%S')

        id_tayangan: str | None = request.data.get('id_tayangan', None)
        if not id_tayangan:
            raise BadRequestException('id_tayangan is required.')

        TayanganTerunduhRepository().delete_one(id_tayangan=id_tayangan,
                                                username=user.username, timestamp=datetime_timestamp)

        data_json = get_all_tayangan_by_username_json(username=user.username)

        return Response(message='Success delete downloads!', data=data_json, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        user: Pengguna | None = get_user(request=request)

        if not user:
            raise UnauthorizedException('Must login to access downloads.')

        timestamp: str | None = request.data.get('timestamp', None)
        if not timestamp:
            raise BadRequestException('Timetamp is required.')
        datetime_timestamp: datetime = datetime.strptime(
            timestamp, '%Y-%m-%dT%H:%M:%S')

        id_tayangan: str | None = request.data.get('id_tayangan', None)
        if not id_tayangan:
            raise BadRequestException('id_tayangan is required.')

        TayanganTerunduhRepository().create(id_tayangan=id_tayangan,
                                            username=user.username, timestamp=datetime_timestamp)

        data_json = get_all_tayangan_by_username_json(username=user.username)

        return Response(message='Success add downloads!', data=data_json, status=status.HTTP_200_OK)
