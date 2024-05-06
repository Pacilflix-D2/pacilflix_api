from core.models.series import Series
from core.repositories.database import Database
from core.utils.exceptions.not_found import NotFoundException


class SeriesRepository(Database):
    def find_all(self) -> list[Series]:
        try:
            series_tuples = self.select('SELECT * FROM series')
        except:
            raise NotFoundException('Cannot find series.')

        result: list[Series] = []
        for series in series_tuples:
            result.append(
                Series(
                    id_tayangan=str(series[0]),
                )
            )

        return result

    def find_by_id(self, id: str) -> Series:
        try:
            tuples = self.select(
                f"SELECT * FROM series WHERE id_tayangan = '{id}'")
        except:
            raise NotFoundException('Cannot find series.')

        if len(tuples) == 0:
            raise NotFoundException('Cannot find series.')

        tuple = tuples[0]

        return Series(id_tayangan=tuple[0])
