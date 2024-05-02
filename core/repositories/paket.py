from core.models.paket import Paket
from core.repositories.database import Database


class PaketRepository(Database):
    def find_by_nama(self, nama: str) -> Paket:
        ...

    def find_all(self) -> list[Paket]:
        ...
