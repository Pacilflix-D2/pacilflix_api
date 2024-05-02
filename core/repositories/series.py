from core.models.series import Series
from core.repositories.database import Database


class SeriesRepository(Database):
    def find_all(self) -> list[Series]:
        ...

    def find_by_id(self, id: str) -> Series:
        ...
