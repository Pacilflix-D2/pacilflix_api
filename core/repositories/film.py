from core.models.film import Film
from core.repositories.database import Database


class FilmRepository(Database):
    def find_all(self) -> list[Film]:
        ...

    def find_by_id(self, id: str) -> Film:
        ...
