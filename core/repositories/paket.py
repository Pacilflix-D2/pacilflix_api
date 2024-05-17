from core.models.paket import Paket
from core.repositories.database import Database
from core.utils.exceptions.not_found import NotFoundException


class PaketRepository(Database):
    def find_by_nama(self, nama: str) -> Paket:
        try:
            tuples = self.select(f"SELECT * FROM paket WHERE nama = '{nama}'")
        except:
            raise NotFoundException('Cannot find package.')

        if len(tuples) == 0:
            raise NotFoundException('Cannot find package.')

        _tuple = tuples[0]

        return Paket(
            nama=_tuple[0],
            harga=_tuple[1],
            resolusi_layar=_tuple[2],
            perangkat=str(_tuple[3]),
        )

    def find_all(self) -> list[Paket]:
        try:
            tuples = self.select("SELECT * FROM paket")
        except:
            raise NotFoundException('Cannot find package.')

        packages = []

        for _tuple in tuples:
            packages.append(Paket(
                nama=_tuple[0],
                harga=_tuple[1],
                resolusi_layar=_tuple[2],
                perangkat=str(_tuple[3]),

            ))

        return packages
