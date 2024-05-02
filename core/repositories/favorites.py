from datetime import datetime
from core.models.favorite import Favorite
from core.repositories.database import Database


class FavoriteRepository(Database):
    def find_by_pk(self, timestamp: datetime, username: str) -> Favorite:
        ...

    def find_by_username(self, id_username: str) -> list[Favorite]:
        ...

    def find_all(self) -> list[Favorite]:
        ...
