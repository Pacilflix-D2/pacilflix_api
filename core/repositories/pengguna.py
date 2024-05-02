from core.models.pengguna import Pengguna
from core.repositories.database import Database


class PenggunaRepository(Database):
    def find_by_username(self, username: str) -> Pengguna:
        ...

    def create(self, username: str, password: str, negara_asal: str, id_tayangan: str | None = None) -> Pengguna:
        ...
