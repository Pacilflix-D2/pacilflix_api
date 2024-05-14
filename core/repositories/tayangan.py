from core.models.tayangan import Tayangan
from core.repositories.database import Database
from core.utils.exceptions.not_found import NotFoundException


class TayanganRepository(Database):
    def find_by_id(self, id: str) -> Tayangan:
        try:
            tuples = self.select(f"SELECT * FROM tayangan WHERE id = '{id}'")
        except:
            raise NotFoundException('Cannot find shows.')

        if len(tuples) == 0:
            raise NotFoundException('Cannot find shows.')

        tuple = tuples[0]

        return Tayangan(
            id=str(tuple[0]),
            judul=tuple[1],
            sinopsis=tuple[2],
            asal_negara=tuple[3],
            sinopsis_trailer=tuple[4],
            url_video_trailer=tuple[5],
            release_date_trailer=tuple[6],
            id_sutradara=str(tuple[7])
        )

    def find_all(self) -> list[Tayangan]:
        try:
            tayangan_tuples = self.select(
                'SELECT * FROM tayangan')
        except:
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

    def find_top_10_tayangan_global(self) -> list[Tayangan]:
        try:
            tayangan_tuples = self.select(
                'SELECT * FROM tayangan ORDER BY judul LIMIT 10')
        except:
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
        try:
            tayangan_tuples = self.select(
                f"SELECT * FROM tayangan WHERE asal_negara = '{country}'")
        except:
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

    def find_by_judul(self, judul: str) -> list[Tayangan]:
        try:
            tuples = self.select(
                f"SELECT * FROM tayangan WHERE LOWER(judul) LIKE LOWER('%{judul}%') ORDER BY judul")
        except Exception as error:
            raise NotFoundException(str(error))

        result: list[Tayangan] = []
        for tuple in tuples:
            result.append(
                Tayangan(
                    id=str(tuple[0]),
                    judul=tuple[1],
                    sinopsis=tuple[2],
                    asal_negara=tuple[3],
                    sinopsis_trailer=tuple[4],
                    url_video_trailer=tuple[5],
                    release_date_trailer=tuple[6],
                    id_sutradara=str(tuple[7]),
                )
            )

        return result
