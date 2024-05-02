from core.models.base import BaseModel


class PerusahaanProduksi(BaseModel):
    def __init__(self, nama: str) -> None:
        self.nama = nama
