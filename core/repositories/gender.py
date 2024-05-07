from core.models.gender import Genre
from core.repositories.database import Database
from core.utils.exceptions.not_found import NotFoundException


class GenreRepository(Database):
    def find_by_id_tayangan(self, id_tayangan: str) -> list[Genre]:
        try:
            tuples = self.select('SELECT * FROM genre_tayangan')
        except:
            raise NotFoundException('Cannot find genres.')

        result: list[Genre] = []
        for tuple in tuples:
            result.append(
                Genre(
                    id_tayangan=str(tuple[0]),
                    genre=tuple[1]
                )
            )

        return result
