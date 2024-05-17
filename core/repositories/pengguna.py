from core.models.pengguna import Pengguna
from core.repositories.database import Database
from core.utils.exceptions.internal_server_error import InternalServerException


class PenggunaRepository(Database):
    def find_by_username(self, username: str) -> Pengguna | None:
        try:
            pengguna_tuples = self.select(
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
        new_user = Pengguna(username=username, password=password,
                            negara_asal=negara_asal, id_tayangan=id_tayangan)

        try:
            if id_tayangan:
                self.insert(
                    f"INSERT INTO PENGGUNA (username, password, id_tayangan, negara_asal) VALUES ('{username}', '{password}', '{id_tayangan}', '{negara_asal}')")
            else:  # tanpa id tayangan
                self.insert(
                    f"INSERT INTO PENGGUNA (username, password, negara_asal) VALUES ('{username}', '{password}', '{negara_asal}')")
        except Exception as e:
            print(e)
            raise InternalServerException(e)

        return new_user
