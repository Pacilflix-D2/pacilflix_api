from core.models.pengguna import Pengguna
from core.repositories.database import Database


class PenggunaRepository(Database):
    def find_by_username(self, username: str) -> Pengguna | None:
        try:
            pengguna_tuples = self.query(
                f"SELECT * from pengguna WHERE username = '{username}'")
        except:
            return None

        if len(pengguna_tuples) == 0:
            return None

        pengguna_tuple = pengguna_tuples[0]

        return Pengguna(
            username=pengguna_tuple[0],
            password=pengguna_tuple[1],
            id_tayangan=str(pengguna_tuple[2]),
            negara_asal=pengguna_tuple[3]
        )

    def create(self, username: str, password: str, negara_asal: str, id_tayangan: str | None = None) -> Pengguna:
        ...
