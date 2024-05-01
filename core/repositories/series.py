from core.repositories.database import Database


class SeriesRepository(Database):
    def find_all(self):
        ...

    def find_by_id(self, id: str):
        ...
