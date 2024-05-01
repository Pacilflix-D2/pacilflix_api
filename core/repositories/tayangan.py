from core.repositories.database import Database


class TayanganRepository(Database):
    def find_top_10_tayangan_global(self):
        ...

    def find_top_tayangan_from_user_country(self, country: str):
        ...
