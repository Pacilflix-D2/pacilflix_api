from typing import Literal

from core.models.base import BaseModel


class Contributors(BaseModel):
    def __init__(self, id: str, nama: str, jenis_kelamin: Literal[0, 1], kewarganegaraan: str) -> None:
        self.id = id
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin
        self.kewarganegaraan = kewarganegaraan
