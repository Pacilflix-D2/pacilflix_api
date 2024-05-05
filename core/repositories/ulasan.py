from datetime import datetime
from core.models.ulasan import Ulasan
from core.repositories.database import Database
from core.utils.exceptions.not_found import NotFoundException


class UlasanRepository(Database):
    def find_one(self, username: str, timestamp: datetime) -> Ulasan:
        ...

    def find_all(self) -> list[Ulasan]:
        ...

    def find_by_id_tayangan(self, id_tayangan: str) -> list[Ulasan]:
        try:
            print('hi')
            ulasan_tuples = self.query(
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
