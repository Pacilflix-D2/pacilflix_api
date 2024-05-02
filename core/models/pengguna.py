from core.models.base import BaseModel


class Pengguna(BaseModel):
    def __init__(self, username: str, password: str, id_tayangan: str, negara_asal: str) -> None:
        self.username = username
        self.password = password
        self.id_tayangan = id_tayangan
        self.negara_asal = negara_asal
