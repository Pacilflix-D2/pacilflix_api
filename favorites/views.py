from datetime import datetime
from typing import Any
from rest_framework.views import APIView
from rest_framework.request import Request
from core.models.favorite import Favorite
from core.models.pengguna import Pengguna
from core.models.tayangan_favorit import TayanganFavorit
from core.repositories.favorites import FavoriteRepository
from core.repositories.tayangan import TayanganRepository
from core.repositories.tayangan_favorit import TayanganFavoritRepository
from core.utils.exceptions.bad_request import BadRequestException
from core.utils.exceptions.unauthorized import UnauthorizedException
from core.utils.get_user import get_user
from core.utils.response import Response
from rest_framework import status


class FavoriteListView(APIView):
    def get(self, request: Request) -> Response:
        user: Pengguna | None = get_user(request=request)

        if not user:
            raise UnauthorizedException('Must login to access favorite.')

        daftar_favorit_user: list[Favorite] = FavoriteRepository(
        ).find_by_username(username=user.username)

        data_json = [daftar_favorit.to_json()
                     for daftar_favorit in daftar_favorit_user]

        return Response(message='Success get daftar favorit!', data=data_json, status=status.HTTP_200_OK)

    def delete(self, request: Request) -> Response:
        ...


class FavoriteListDetailView(APIView):
    def get(self, request: Request) -> Response:
        tayangan_repository = TayanganRepository()

        user: Pengguna | None = get_user(request=request)

        if not user:
            raise UnauthorizedException('Must login to access favorite.')

        timestamp: str | None = request.data.get('timestamp', None)
        if not timestamp:
            raise BadRequestException('Timetamp is required.')
        datetime_timestamp = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S')

        daftar_favorit_user: Favorite = FavoriteRepository().find_one(
            timestamp=datetime_timestamp, username=user.username)

        favorit_shows: list[TayanganFavorit] = TayanganFavoritRepository(
        ).find_by_daftar_favorit(daftar_favorit=daftar_favorit_user)

        favorites_json_list: list[dict[str, Any]] = []
        for favorit_show in favorit_shows:
            favorit_show_json = favorit_show.to_json()
            favorit_show_json.pop('id_tayangan')
            favorit_show_json.pop('username')

            show = tayangan_repository.find_by_id(id=favorit_show.id_tayangan)
            show_json = show.to_json()

            favorites_json_list.append({
                **favorit_show_json,
                'id': show_json['id'],
                'judul': show_json['judul']
            })

        data_json = {
            'judul': daftar_favorit_user.judul,
            'favorites': favorites_json_list
        }

        return Response(message='Success get daftar favorit', data=data_json, status=status.HTTP_200_OK)

    def delete(self, request: Request) -> Response:
        ...
