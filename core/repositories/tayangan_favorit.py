from datetime import datetime
from core.models.favorite import Favorite
from core.models.tayangan_favorit import TayanganFavorit
from core.repositories.database import Database
from core.utils.exceptions.internal_server_error import InternalServerException
from core.utils.exceptions.not_found import NotFoundException


class TayanganFavoritRepository(Database):
    def find_all(self) -> list[TayanganFavorit]:
        ...

    def find_by_daftar_favorit(self, daftar_favorit: Favorite) -> list[TayanganFavorit]:
        try:
            tuples = self.select(
                f"SELECT * FROM TAYANGAN_MEMILIKI_DAFTAR_FAVORIT WHERE username = '{daftar_favorit.username}' AND timestamp = '{daftar_favorit.timestamp}'")
        except Exception as error:
            raise NotFoundException(error)

        return [
            TayanganFavorit(
                id_tayangan=str(tuple[0]),
                timestamp=tuple[1],
                username=tuple[2]
            ) for tuple in tuples
        ]

    def delete_by_username_timestamp(self, username: str, timestamp: datetime) -> None:
        try:
            converted_timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')
            self.delete(
                f"DELETE FROM TAYANGAN_MEMILIKI_DAFTAR_FAVORIT WHERE username = '{username}' AND timestamp = '{converted_timestamp}'")
        except Exception as error:
            raise InternalServerException(error)

    def delete_one(self, id_tayangan: str, timestamp: datetime, username: str) -> None:
        try:
            self.delete(
                f"DELETE FROM TAYANGAN_MEMILIKI_DAFTAR_FAVORIT WHERE id_tayangan = '{id_tayangan}' AND timestamp = '{timestamp}' AND username = '{username}'")
        except Exception as error:
            raise InternalServerException(error)

    def create_one(self, id_tayangan: str, timestamp: datetime, username: str) -> None:
        try:
            self.insert(
                f"INSERT INTO TAYANGAN_MEMILIKI_DAFTAR_FAVORIT (id_tayangan, timestamp, username) VALUES ('{id_tayangan}', '{timestamp}', '{username}')")
        except Exception as error:
            raise InternalServerException(error)
