from datetime import datetime
from core.models.ulasan import Ulasan
from core.repositories.database import Database


class UlasanRepository(Database):
    def find_one(self, username: str, timestamp: datetime) -> Ulasan:
        ...

    def find_all(self) -> list[Ulasan]:
        ...

    def find_by_id_tayangan(self, id_tayangan: str) -> list[Ulasan]:
        ...

    def find_by_username(self, username: str) -> list[Ulasan]:
        ...
