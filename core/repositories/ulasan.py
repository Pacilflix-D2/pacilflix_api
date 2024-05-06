from datetime import datetime
from core.models.ulasan import Ulasan
from core.repositories.database import Database
from core.utils.exceptions.internal_server_error import InternalServerException
from core.utils.exceptions.not_found import NotFoundException


class UlasanRepository(Database):
    def find_one(self, username: str, timestamp: datetime) -> Ulasan:
        ...

    def find_all(self) -> list[Ulasan]:
        ...

    def find_by_id_tayangan(self, id_tayangan: str) -> list[Ulasan]:
        try:
            print('hi')
            ulasan_tuples = self.select(
                f"SELECT * FROM ulasan WHERE id_tayangan = '{id_tayangan}'")
            print(ulasan_tuples)
        except:
            raise NotFoundException('Cannot find ulasan.')

        if (len(ulasan_tuples) == 0):
            raise NotFoundException('Cannot find ulasan.')

        result: list[Ulasan] = []
        for ulasan in ulasan_tuples:
            result.append(Ulasan(
                id_tayangan=str(ulasan[0]),
                username=ulasan[1],
                timestamp=ulasan[2],
                rating=ulasan[3],
                deskripsi=ulasan[4]
            )
            )

        return result

    def find_by_username(self, username: str) -> list[Ulasan]:
        ...

    def create(self, id_tayangan: str, username: str, timestamp: datetime, rating: int, deskripsi: str | None) -> Ulasan:
        new_ulasan = Ulasan(
            id_tayangan=id_tayangan,
            username=username,
            timestamp=timestamp,
            rating=rating,
            deskripsi=deskripsi
        )

        try:
            if deskripsi:
                self.insert(
                    f"INSERT INTO ULASAN (id_tayangan, username, timestamp, rating, deskripsi) VALUES ('{id_tayangan}', '{username}', '{timestamp}', {rating}, '{deskripsi}')")
            else:
                self.insert(
                    f"INSERT INTO ULASAN (id_tayangan, username, timestamp, rating) VALUES ('{id_tayangan}', '{username}', '{timestamp}', {rating})")
        except Exception as e:
            print(e)
            raise InternalServerException('Failed to create user.')

        return new_ulasan
