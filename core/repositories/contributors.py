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

    def find_all(self) -> list[Contributor]:
        ...
