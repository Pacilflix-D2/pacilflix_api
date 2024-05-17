from datetime import date
from core.models.base import BaseModel


class Film(BaseModel):
    def __init__(self, id_tayangan: str, url_video_film: str, release_date_film: date, durasi_film: int) -> None:
        self.id_tayangan = id_tayangan
        self.url_video_film = url_video_film
        self.release_date_film = release_date_film
        self.durasi_film = durasi_film
