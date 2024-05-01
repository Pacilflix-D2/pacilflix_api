from core.repositories.database import Database


class ContributorRepository(Database):
    def find_by_id(self, id: str):
        ...

    def find_all(self):
        ...
