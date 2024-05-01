from core.repositories.database import Database


class PenggunaRepository(Database):
    def find_user_by_id(self, id: str):
        ...

    def find_user_by_username(self, username: str):
        ...

    def create_user(self, username: str, password: str, id_tayangan: str | None = None, negara_asal: str):
        ...
