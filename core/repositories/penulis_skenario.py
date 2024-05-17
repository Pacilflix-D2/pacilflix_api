from core.models.penulis_skenario import PenulisSkenario
from core.repositories.database import Database
from core.utils.exceptions.not_found import NotFoundException


class PenulisSkenarioRepository(Database):
    def find_by_id_tayangan(self, id_tayangan: str) -> list[PenulisSkenario]:
        try:
            tuples = self.select(
                f'''SELECT C.id, C.nama, C.jenis_kelamin, C.kewarganegaraan
                FROM contributors C, penulis_skenario P, memainkan_tayangan M
                WHERE C.id = P.id AND P.id = M.id_pemain AND M.id_tayangan = '{id_tayangan}';''')
        except:
            raise NotFoundException('Cannot find writers.')

        result: list[PenulisSkenario] = []
        for tuple in tuples:
            result.append(
                PenulisSkenario(
                    id_contributor=str(tuple[0]),
                    nama=tuple[1],
                    jenis_kelamin=tuple[2],
                    kewarganegaraan=tuple[3],
                )
            )

        return result
