from core.models.pemain import Pemain
from core.repositories.database import Database
from core.utils.exceptions.not_found import NotFoundException


class PemainRepository(Database):
    def find_by_id_tayangan(self, id_tayangan: str) -> list[Pemain]:
        try:
            tuples = self.select(
                f'''SELECT C.id, C.nama, C.jenis_kelamin, C.kewarganegaraan
                FROM contributors C, pemain P, memainkan_tayangan M
                WHERE C.id = P.id AND P.id = M.id_pemain AND M.id_tayangan = '{id_tayangan}';''')
        except:
            raise NotFoundException('Cannot find players.')

        result: list[Pemain] = []
        for tuple in tuples:
            result.append(
                Pemain(
                    id_contributor=str(tuple[0]),
                    nama=tuple[1],
                    jenis_kelamin=tuple[2],
                    kewarganegaraan=tuple[3],
                )
            )

        return result
