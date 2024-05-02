from core.models.base import BaseModel


class Paket(BaseModel):
    def __init__(self, nama: str, harga: int, resolusi_layar: str) -> None:
        self.nama = nama
        self.harga = harga
        self.resolusi_layar = resolusi_layar
