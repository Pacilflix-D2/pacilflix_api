from core.models.base import BaseModel


class PenulisSkenario(BaseModel):
    def __init__(self, id_contributor: str, nama: str, jenis_kelamin: int, kewarganegaraan: str) -> None:
        self.id_contributor = id_contributor
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin
        self.kewarganegaraan = kewarganegaraan
