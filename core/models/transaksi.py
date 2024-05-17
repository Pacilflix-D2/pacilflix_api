from typing import Any

from core.models.base import BaseModel


class Transaksi(BaseModel):
    def __init__(self, username: str, name: str, start: str, end: str, metode: str, tglpembayaran: str, total: int):
        self.username = username
        self.name = name
        self.start = start
        self.end = end
        self.metode = metode
        self.tglpembayaran = tglpembayaran
        self.total = total

    def to_json(self) -> dict[str, Any]:
        return {
            'username': self.username,
            'name': self.name,
            'start': self.start,
            'end': self.end,
            'metode': self.metode,
            'tglpembayaran': self.tglpembayaran,
            'total': self.total
        }

    def get_nama(self) -> str:
        return self.name

    def get_start(self) -> str:
        return self.start

    def get_end(self) -> str:
        return self.end

    def get_metode(self) -> str:
        return self.metode

    def get_tgl_pembayaran(self) -> str:
        return self.tglpembayaran

    def get_total(self) -> int:
        return self.total

    def get_username(self) -> str:
        return self.username
