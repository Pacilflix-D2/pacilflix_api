from core.models.tayangan import Tayangan
from core.repositories.database import Database


class TayanganRepository(Database):
    def find_by_id(self, id: str) -> Tayangan:
        ...

    def find_all(self) -> list[Tayangan]:
        ...

    def find_top_10_tayangan_global(self) -> list[Tayangan]:
        ...

    def find_top_tayangan_from_user_country(self, country: str) -> list[Tayangan]:
        ...
