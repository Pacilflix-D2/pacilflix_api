from datetime import datetime
from core.models.base import BaseModel


class Ulasan(BaseModel):
    def __init__(self, id_tayangan: str, username: str, timestamp: datetime, rating: int, deskripsi: str | None) -> None:
        self.id_tayangan = id_tayangan
        self.username = username
        self.timestamp = timestamp
        self.rating = rating
        self.deskripsi = deskripsi
