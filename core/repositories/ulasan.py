from datetime import datetime
from core.repositories.database import Database


class UlasanRepository(Database):
    def find_one(self, username: str, timestamp: datetime):
        ...

    def find_all(self):
        ...
