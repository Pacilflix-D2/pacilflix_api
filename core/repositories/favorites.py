from datetime import datetime
from core.models.favorite import Favorite
from core.repositories.database import Database
from core.repositories.tayangan_favorit import TayanganFavoritRepository
from core.utils.exceptions.internal_server_error import InternalServerException
from core.utils.exceptions.not_found import NotFoundException


class FavoriteRepository(Database):
    def find_one(self, timestamp: datetime, username: str) -> Favorite:
        try:
            tuples = self.select(
                f"SELECT * FROM daftar_favorit WHERE username = '{username}' AND timestamp = '{timestamp}'")
        except Exception as error:
            raise NotFoundException(error)

        if len(tuples) == 0:
            raise NotFoundException('Cannot find daftar favorit.')

        tuple = tuples[0]

        return Favorite(
            timestamp=tuple[0],
            username=tuple[1],
            judul=tuple[2]
        )

    def find_by_username(self, username: str) -> list[Favorite]:
        try:
            tuples = self.select(
                f"SELECT * FROM daftar_favorit WHERE username = '{username}'")
        except Exception as error:
            raise NotFoundException(error)

        result: list[Favorite] = []
        for tuple in tuples:
            result.append(Favorite(
                timestamp=tuple[0],
                username=tuple[1],
                judul=tuple[2]
            ))

        return result

    def find_all(self) -> list[Favorite]:
        ...

    def delete_one(self, timestamp: datetime, username: str) -> None:
        try:
            TayanganFavoritRepository(
            ).delete_by_username_timestamp(username=username, timestamp=timestamp)
        except Exception as error:
            raise InternalServerException(error)

        try:
            converted_timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')
            self.delete(
                f"DELETE FROM daftar_favorit WHERE timestamp = '{converted_timestamp}' AND username = '{username}'")
        except Exception as error:
            raise NotFoundException(error)
