from typing import Any

from core.models.tayangan_terunduh import TayanganTerunduh
from core.repositories.tayangan import TayanganRepository
from core.repositories.tayangan_terunduh import TayanganTerunduhRepository


def get_all_tayangan_by_username_json(username: str):
    downloads: list[TayanganTerunduh] = TayanganTerunduhRepository(
    ).find_by_username(username=username)

    data_json: list[dict[str, Any]] = [
        {
            **download.to_json(),
            "judul": TayanganRepository().find_by_id(id=download.id_tayangan).judul
        }
        for download in downloads
    ]

    return data_json
