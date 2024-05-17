from datetime import datetime
from rest_framework.views import APIView
from rest_framework.request import Request
from core.models.pengguna import Pengguna
from core.repositories.favorites import FavoriteRepository
from core.repositories.tayangan_favorit import TayanganFavoritRepository
from core.utils.exceptions.bad_request import BadRequestException
from core.utils.exceptions.unauthorized import UnauthorizedException
from core.utils.get_user import get_user
from core.utils.response import Response
from rest_framework import status

from favorites.services import get_daftar_favorit_by_username_json, get_tayangan_favorit_list_by_username_timestamp_json


class FavoriteListView(APIView):
    def get(self, request: Request) -> Response:
        user: Pengguna | None = get_user(request=request)

        if not user:
            raise UnauthorizedException('Must login to access favorite.')

        data_json = get_daftar_favorit_by_username_json(username=user.username)

        return Response(message='Success get daftar favorit!', data=data_json, status=status.HTTP_200_OK)

    def delete(self, request: Request) -> Response:
        user: Pengguna | None = get_user(request=request)
        if not user:
            raise UnauthorizedException('Must login to access favorite.')

        timestamp: str | None = request.data.get('timestamp', None)
        if not timestamp:
            raise BadRequestException('Timetamp is required.')
        datetime_timestamp = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S')

        FavoriteRepository().delete_one(timestamp=datetime_timestamp, username=user.username)

        data_json = get_daftar_favorit_by_username_json(username=user.username)

        return Response(message='Success delete favorite repository!', data=data_json, status=status.HTTP_200_OK)


class FavoriteListDetailView(APIView):
    def get(self, request: Request) -> Response:
        user: Pengguna | None = get_user(request=request)

        if not user:
            raise UnauthorizedException('Must login to access favorite.')

        timestamp: str | None = request.query_params.get('timestamp', None)
        if not timestamp:
            raise BadRequestException('Timetamp is required.')
        datetime_timestamp = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S')

        data_json = get_tayangan_favorit_list_by_username_timestamp_json(
            timestamp=datetime_timestamp, username=user.username)

        return Response(message='Success get daftar favorit', data=data_json, status=status.HTTP_200_OK)

    def delete(self, request: Request) -> Response:
        user: Pengguna | None = get_user(request=request)

        if not user:
            raise UnauthorizedException('Must login to access favorite.')

        timestamp: str | None = request.data.get('timestamp', None)
        if not timestamp:
            raise BadRequestException('Timetamp is required.')
        datetime_timestamp = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S')

        id_tayangan: str | None = request.data.get('id_tayangan', None)
        if not id_tayangan:
            raise BadRequestException('id_tayangan is required.')

        TayanganFavoritRepository().delete_one(id_tayangan=id_tayangan,
                                               timestamp=datetime_timestamp, username=user.username)

        data_json = get_tayangan_favorit_list_by_username_timestamp_json(
            timestamp=datetime_timestamp, username=user.username)

        return Response(message='Success delete tayangan favorit!', data=data_json, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        user: Pengguna | None = get_user(request=request)

        if not user:
            raise UnauthorizedException('Must login to access favorite.')

        id_tayangan = request.data.get('id_tayangan', None)
        if not id_tayangan:
            raise BadRequestException('required id tayangan')

        timestamp = request.data.get('timestamp', None)
        if not timestamp:
            raise BadRequestException('required timestamp')

        datetime_timestamp = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S')

        TayanganFavoritRepository().create_one(id_tayangan=id_tayangan,
                                               timestamp=datetime_timestamp, username=user.username)

        return Response(message='Success add tayangan to favorit!')
