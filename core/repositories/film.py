from core.models.film import Film
from core.repositories.database import Database
from core.utils.exceptions.not_found import NotFoundException


class FilmRepository(Database):
    def find_all(self) -> list[Film]:
        try:
            film_tuples = self.query('SELECT * FROM film')
        except:
            raise NotFoundException('Cannot find films.')
        # print('WOW')
        # print(film_tuples)

        result: list[Film] = []
        for film in film_tuples:
            # print('HERE')
            # print(film[3])
            # print(type(film[3]))

            result.append(
                Film(
                    id_tayangan=str(film[0]),
                    url_video_film=film[1],
                    release_date_film=film[2],
                    durasi_film=film[3],
                )
            )

        return result

    def find_by_id(self, id_tayangan: str) -> Film:
        try:
            film_tuples = self.query(
                f"SELECT * FROM film WHERE id_tayangan = '{id_tayangan}'")
        except:
            raise NotFoundException('Cannot find film.')

        print('LEN')
        print(len(film_tuples))

        if (len(film_tuples) == 0):
            print('throwed')
            raise NotFoundException('Cannot found film.')

        film_tuple = film_tuples[0]

        result: Film = Film(
            id_tayangan=str(film_tuple[0]),
            url_video_film=film_tuple[1],
            release_date_film=film_tuple[2],
            durasi_film=film_tuple[3],
        )

        return result
