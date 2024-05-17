from datetime import datetime
from core.models.tayangan_terunduh import TayanganTerunduh
from core.repositories.database import Database
from core.utils.exceptions.internal_server_error import InternalServerException


class TayanganTerunduhRepository(Database):
    def find_by_username(self, username: str) -> list[TayanganTerunduh]:
        try:
            tuples = self.select(
                f"SELECT * FROM tayangan_terunduh WHERE username = '{username}'")
        except Exception as error:
            raise InternalServerException(error)

        return [
            TayanganTerunduh(
                id_tayangan=tuple[0],
                username=tuple[1],
                timestamp=tuple[2]) for tuple in tuples
        ]

    def delete_one(self, id_tayangan: str, username: str, timestamp: datetime) -> None:
        try:
            self.delete(
                f"DELETE FROM tayangan_terunduh WHERE id_tayangan = '{id_tayangan}' AND username = '{username}' AND timestamp = '{timestamp}'")
        except Exception as error:
            raise InternalServerException(error)

    def create(self, id_tayangan: str, username: str, timestamp: datetime) -> TayanganTerunduh:
        new_unduh = TayanganTerunduh(
            id_tayangan=id_tayangan,
            username=username,
            timestamp=timestamp
        )

        try:
            self.insert(
                f"INSERT INTO tayangan_terunduh (id_tayangan, username, timestamp) VALUES ('{id_tayangan}', '{username}', '{timestamp}')")
        except Exception as error:
            raise InternalServerException(error)

        return new_unduh
