from core.models.contributor import Contributor
from core.repositories.database import Database


class ContributorRepository(Database):
    def find_by_id(self, id: str) -> Contributor:
        ...

    def find_all(self) -> list[Contributor]:
        ...
