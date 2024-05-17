from datetime import date
from typing import Any

from core.models.transaksi import Transaksi
from core.repositories.database import Database
from core.utils.exceptions.not_found import NotFoundException


class TransaksiRepository(Database):
    def get_total_payment(self, package_name):
        if package_name == 'Paket Basic':
            return 99900
        elif package_name == 'Paket Standard':
            return 149900
        else:
            return 219900

    def find_by_username(self, username: str) -> list[dict[str, Any]]:
        try:
            tuples = self.select(f"SELECT * FROM transaction WHERE username = '{username}'")
        except Exception as error:
            raise NotFoundException(error)

        if len(tuples) == 0:
            raise NotFoundException('Cannot find transaction.')

        history = []

        for _tuple in tuples:
            history.append({
                "packageName": _tuple[3],
                "startDate": str(_tuple[1]),
                "endDate": str(_tuple[2]),
                "paymentMethod": _tuple[4],
                "paymentDate": str(_tuple[5]),
                "totalPayment": self.get_total_payment(_tuple[3])
            })

        return history

    def find_all(self) -> list[Transaksi]:
        try:
            tuples = self.select("SELECT * FROM transaksi")
        except:
            raise NotFoundException('Cannot find transaction.')

        history = []

        for _tuple in tuples:
            history.append(Transaksi(
                username=_tuple[0],
                name=_tuple[1],
                start=str(_tuple[2]),
                end=str(_tuple[3]),
                metode=_tuple[4],
                tglpembayaran=str(_tuple[5]),
                total=_tuple[6]
            ))

        return history

    def insert_data(self, transaksi: Transaksi) -> None:
        if not isinstance(transaksi, Transaksi):
            raise TypeError('Expected transaksi to be an instance of Transaksi')
        try:
            self.insert(f"INSERT INTO transaction VALUES ('{transaksi.username}', '{transaksi.start}', '{transaksi.end}', '{transaksi.name}', '{transaksi.metode}', '{transaksi.tglpembayaran}')")
        except Exception as e:
            raise NotFoundException(e)

    def get_active_subscription(self, username: str) -> dict:
        current_date = date.today().strftime('%Y-%m-%d')
        try:
            _tuple = self.select(f"""
                SELECT p.*, t.start_date_time, t.end_date_time
                FROM transaction t
                JOIN paket p ON t.nama_paket = p.nama
                WHERE t.username = '{username}' AND t.end_date_time >= '{current_date}'
                ORDER BY t.end_date_time DESC
            """)
        except Exception as e:
            raise NotFoundException(e)

        if len(_tuple) == 0 or len(_tuple[0]) < 5:
            raise NotFoundException('No active subscription found.')

        active_subscription = {
            "name": _tuple[0][0],
            "price": _tuple[0][1],
            "resolution": _tuple[0][2],
            "supportedDevices": self.get_supported_device(str(_tuple[0][0])),
            "startDate": str(_tuple[0][3]),
            "endDate": str(_tuple[0][4]),
        }

        return active_subscription

    def get_supported_device(self, package_name: str) -> list[str]:
        if package_name == 'Paket Basic':
            return ['Smartphone']
        elif package_name == 'Paket Standard':
            return ['Smartphone', 'Tablet', 'PC']
        else:
            return ['Smartphone', 'Tablet', 'PC', 'Smart TV']
