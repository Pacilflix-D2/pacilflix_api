from core.repositories.database import Database


class PenggunaRepository(Database):
    def find_by_id(self, id: str):
        ...

    def find_by_username(self, username: str):
        ...

    def create(self, username: str, password: str, id_tayangan: str | None = None, negara_asal: str):
        ...
