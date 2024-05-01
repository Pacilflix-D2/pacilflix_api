from core.repositories.database import Database


class PaketRepository(Database):
    def find_by_nama(self, nama: str):
        ...

    def find_all(self):
        ...
