from core.repositories.database import Database


class FavoriteRepository(Database):
    def find_by_username(self, id_username: str):
        ...

    def find_all(self):
        ...
