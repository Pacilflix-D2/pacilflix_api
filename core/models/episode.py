from datetime import date

from core.models.base import BaseModel


class Episode(BaseModel):
    def __init__(self, id_series: str, sub_judul: str, sinopsis: str, durasi: int, url_video: str, release_date: date) -> None:
        self.id_series = id_series
        self.sub_judul = sub_judul
        self.sinopsis = sinopsis
        self.durasi = durasi
        self.url_video = url_video
        self.release_date = release_date
