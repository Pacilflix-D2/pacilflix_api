from datetime import datetime
from core.models.base import BaseModel


class TayanganTerunduh(BaseModel):
    def __init__(self, id_tayangan: str, username: str, timestamp: datetime) -> None:
        self.id_tayangan = id_tayangan
        self.username = username
        self.timestamp = timestamp
