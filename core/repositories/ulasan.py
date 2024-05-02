from datetime import datetime
from core.models.ulasan import Ulasan
from core.repositories.database import Database


class UlasanRepository(Database):
    def find_one(self, username: str, timestamp: datetime) -> Ulasan:
        ...

    def find_all(self) -> list[Ulasan]:
        ...
