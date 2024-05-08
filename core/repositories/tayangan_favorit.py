from core.models.favorite import Favorite
from core.models.tayangan_favorit import TayanganFavorit
from core.repositories.database import Database
from core.utils.exceptions.not_found import NotFoundException


class TayanganFavoritRepository(Database):
    def find_all(self) -> list[TayanganFavorit]:
        ...

    def find_by_daftar_favorit(self, daftar_favorit: Favorite) -> list[TayanganFavorit]:
        try:
            tuples = self.select(
                f"SELECT * FROM TAYANGAN_MEMILIKI_DAFTAR_FAVORIT WHERE username = '{daftar_favorit.username}' AND timestamp = '{daftar_favorit.timestamp}'")
        except Exception as error:
            raise NotFoundException(error)

        return [
            TayanganFavorit(
                id_tayangan=str(tuple[0]),
                timestamp=tuple[1],
                username=tuple[2]
            ) for tuple in tuples
        ]
