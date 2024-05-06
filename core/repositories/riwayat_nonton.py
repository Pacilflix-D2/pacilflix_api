from datetime import datetime
from core.models.riwayat_nonton import RiwayatNonton
from core.repositories.database import Database
from core.utils.exceptions.internal_server_error import InternalServerException
from core.utils.exceptions.not_found import NotFoundException


class RiwayatNontonRepository(Database):
    def find_by_id_tayangan(self, id_tayangan: str) -> list[RiwayatNonton]:
        try:
            tuples = self.query(
                f"SELECT * FROM riwayat_nonton WHERE id_tayangan = '{id_tayangan}'")
        except:
            raise NotFoundException('Cannot find watch histories.')

        result: list[RiwayatNonton] = []
        for tuple in tuples:
            result.append(
                RiwayatNonton(
                    id_tayangan=str(tuple[0]),
                    username=tuple[1],
                    start_date_time=tuple[2],
                    end_date_time=tuple[3]
                )
            )

        return result

    def find_by_id_tayangan_last_week(self, id_tayangan: str) -> list[RiwayatNonton]:
        try:
            tuples = self.query(
                f"SELECT * FROM riwayat_nonton WHERE id_tayangan = '{id_tayangan}' AND end_date_time >= NOW() - INTERVAL '7 days'")
        except:
            raise InternalServerException('Failed to find riwayat nonton.')

        result: list[RiwayatNonton] = []
        for tuple in tuples:
            result.append(
                RiwayatNonton(
                    id_tayangan=str(tuple[0]),
                    username=tuple[1],
                    start_date_time=tuple[2],
                    end_date_time=tuple[3]
                )
            )

        return result

    def find_by_watch_time(self, start_date_time: datetime, end_date_time: datetime) -> list[RiwayatNonton]:
        ...

    def find_all(self) -> list[RiwayatNonton]:
        ...

    def find_one(self, username: str, start_date_time: datetime) -> RiwayatNonton:
        ...
