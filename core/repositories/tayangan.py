from core.models.tayangan import Tayangan
from core.repositories.database import Database
from core.utils.exceptions.not_found import NotFoundException


class TayanganRepository(Database):
    def find_by_id(self, id: str) -> Tayangan:
        ...

    def find_all(self) -> list[Tayangan]:
        ...

    def find_top_10_tayangan_global(self) -> list[Tayangan]:
        try:
            tayangan_tuples = self.query(
                'SELECT * FROM tayangan ORDER BY judul LIMIT 10')
        except:
            raise NotFoundException('Cannot find shows.')

        if len(tayangan_tuples) == 0:
            raise NotFoundException('Cannot find shows.')

        result: list[Tayangan] = []
        for tayangan in tayangan_tuples:
            result.append(
                Tayangan(
                    id=str(tayangan[0]),
                    judul=tayangan[1],
                    sinopsis=tayangan[2],
                    asal_negara=tayangan[3],
                    sinopsis_trailer=tayangan[4],
                    url_video_trailer=tayangan[5],
                    release_date_trailer=tayangan[6],
                    id_sutradara=str(tayangan[7]),
                )
            )

        return result

    def find_top_tayangan_from_user_country(self, country: str) -> list[Tayangan]:
        ...
