from datetime import datetime
from core.models.tayangan_favorit import TayanganFavorit
from core.repositories.database import Database


class TayanganFavoritRepository(Database):
    def find_all(self) -> list[TayanganFavorit]:
        ...

    def find_by_username_and_timestamp(self, username: str, timestamp: datetime) -> list[TayanganFavorit]:
        ...
