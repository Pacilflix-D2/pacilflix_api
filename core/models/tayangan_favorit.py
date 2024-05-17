from datetime import datetime
from core.models.base import BaseModel


class TayanganFavorit(BaseModel):
    def __init__(self, id_tayangan: str, timestamp: datetime, username: str) -> None:
        self.id_tayangan = id_tayangan
        self.timestamp = timestamp
        self.username = username
