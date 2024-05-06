from datetime import datetime
from core.models.base import BaseModel


class RiwayatNonton(BaseModel):
    def __init__(self, id_tayangan: str, username: str, start_date_time: datetime, end_date_time: datetime) -> None:
        self.id_tayangan = id_tayangan
        self.username = username
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
