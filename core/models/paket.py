from core.models.base import BaseModel


class Paket(BaseModel):
    def __init__(self, nama: str, harga: int, resolusi_layar: str, perangkat: str) -> None:
        self.nama = nama
        self.harga = harga
        self.resolusi_layar = resolusi_layar
        self.perangkat = perangkat

    def get_nama(self):
        return self.nama

    def get_harga(self):
        return self.harga

    def get_resolusi_layar(self):
        return self.resolusi_layar

    def get_perangkat(self):
        return self.perangkat

    def to_json(self) -> dict:
        return {
            'nama': self.nama,
            'harga': self.harga,
            'resolusi_layar': self.resolusi_layar,
            'perangkat': self.perangkat
        }
