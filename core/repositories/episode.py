from core.models.episode import Episode
from core.repositories.database import Database
from core.utils.exceptions.not_found import NotFoundException


class EpisodeRepository(Database):
    def find_all(self) -> list[Episode]:
        ...

    def find_by_id_series(self, id_series: str) -> list[Episode]:
        try:
            tuples = self.select(
                f"SELECT * FROM episode WHERE id_series = '{id_series}' ORDER BY sub_judul")
        except Exception as e:
            raise NotFoundException(str(e))

        result: list[Episode] = []
        for tuple in tuples:
            result.append(
                Episode(
                    id_series=str(tuple[0]),
                    sub_judul=tuple[1],
                    sinopsis=tuple[2],
                    durasi=tuple[3],
                    url_video=tuple[4],
                    release_date=tuple[5]
                )
            )

        return result

    def find_by_pk(self, id_series: str, sub_judul: str) -> Episode:
        try:
            tuples = self.select(
                f"SELECT * FROM episode WHERE id_series = '{id_series}' AND sub_judul = '{sub_judul}'")
        except Exception as e:
            raise NotFoundException(str(e))

        tuple = tuples[0]

        return Episode(
            id_series=str(tuple[0]),
            sub_judul=tuple[1],
            sinopsis=tuple[2],
            durasi=tuple[3],
            url_video=tuple[4],
            release_date=tuple[5]
        )
