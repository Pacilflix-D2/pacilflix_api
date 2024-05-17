from datetime import datetime
from typing import Any

from core.models.favorite import Favorite
from core.models.tayangan import Tayangan
from core.models.tayangan_favorit import TayanganFavorit
from core.repositories.favorites import FavoriteRepository
from core.repositories.tayangan import TayanganRepository
from core.repositories.tayangan_favorit import TayanganFavoritRepository
from django.conf import settings


def get_daftar_favorit_by_username_json(username: str) -> list[dict[str, Any]]:
    daftar_favorit_user: list[Favorite] = FavoriteRepository(
    ).find_by_username(username=username)

    data_json = [
        {
            **daftar_favorit.to_json(),
            "timezone": settings.TIME_ZONE
        }
        for daftar_favorit in daftar_favorit_user
    ]

    return data_json


def get_tayangan_favorit_list_by_username_timestamp_json(timestamp: datetime, username: str):
    daftar_favorit_user: Favorite = FavoriteRepository().find_one(
        timestamp=timestamp, username=username)

    favorit_shows: list[TayanganFavorit] = TayanganFavoritRepository(
    ).find_by_daftar_favorit(daftar_favorit=daftar_favorit_user)

    favorites_json_list: list[dict[str, Any]] = []
    for favorit_show in favorit_shows:
        favorit_show_json = favorit_show.to_json()
        favorit_show_json.pop('id_tayangan')
        favorit_show_json.pop('username')

        show: Tayangan = TayanganRepository().find_by_id(id=favorit_show.id_tayangan)
        show_json = show.to_json()

        print(favorit_show.timestamp)

        favorites_json_list.append({
            **favorit_show_json,
            'id': show_json['id'],
            'judul': show_json['judul'],
            "timezone": settings.TIME_ZONE
        })

    data_json = {
        'judul': daftar_favorit_user.judul,
        'favorites': favorites_json_list
    }

    return data_json
