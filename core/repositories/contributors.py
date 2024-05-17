from core.models.contributor import Contributor
from core.repositories.database import Database
from core.utils.exceptions.not_found import NotFoundException


class ContributorRepository(Database):
    def find_by_id(self, id: str) -> Contributor:
        try:
            tuples = self.select(
                f"SELECT * FROM contributors WHERE id = '{id}'")
        except:
            raise NotFoundException('Cannot find contributor.')

        if len(tuples) == 0:
            raise NotFoundException('Cannot find contributor.')

        tuple = tuples[0]

        return Contributor(
            id=str(tuple[0]),
            nama=tuple[1],
            jenis_kelamin=tuple[2],
            kewarganegaraan=tuple[3]
        )

    def find_all(self) -> list[dict]:
        try:
            tuples = self.select(
                """
                SELECT c.id, c.nama, c.jenis_kelamin, c.kewarganegaraan
                FROM contributors c
                """
            )
        except:
            raise NotFoundException('Cannot find any contributors.')

        if len(tuples) == 0:
            raise NotFoundException('Cannot find any contributors.')

        contributors = []
        for tuple in tuples:
            contributor = {
                'id': str(tuple[0]),
                'nama': tuple[1],
                'jenis_kelamin': 'Laki-laki' if tuple[2] == 0 else 'Perempuan',
                'kewarganegaraan': tuple[3],
                'tipe': []
            }

            sutradara = self.select(
                f"SELECT id FROM sutradara WHERE id = '{contributor['id']}'")
            if sutradara:
                contributor['tipe'].append('Sutradara')

            pemain = self.select(
                f"SELECT id FROM pemain WHERE id = '{contributor['id']}'")
            if pemain:
                contributor['tipe'].append('Pemain')

            penulis_skenario = self.select(
                f"SELECT id FROM penulis_skenario WHERE id = '{contributor['id']}'")
            if penulis_skenario:
                contributor['tipe'].append('Penulis Skenario')

            contributors.append(contributor)

        return contributors
