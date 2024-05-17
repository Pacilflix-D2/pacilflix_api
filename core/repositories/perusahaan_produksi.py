from core.models.perusahaan_produksi import PerusahaanProduksi
from core.repositories.database import Database


class PerusahaanRepository(Database):
    def find_by_nama(self, nama: str) -> PerusahaanProduksi:
        ...

    def find_all(self) -> list[PerusahaanProduksi]:
        ...
