from datetime import datetime
from core.models.base import BaseModel


class Favorite(BaseModel):
    def __init__(self, timestamp: datetime, username: str, judul: str) -> None:
        self.timestamp = timestamp
        self.username = username
        self.judul = judul
