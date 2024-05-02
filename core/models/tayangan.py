from datetime import date
from core.models.base import BaseModel


class Tayangan(BaseModel):
    def __init__(self, id: str, judul: str, sinopsis: str, asal_negara: str, sinopsis_trailer: str, url_video_trailer: str, release_date_trailer: date, id_sutradara: str) -> None:
        self.id = id
        self.judul = judul
        self.sinopsis = sinopsis
        self.asal_negara = asal_negara
        self.sinopsis_trailer = sinopsis_trailer
        self.url_video_trailer = url_video_trailer
        self.release_date_trailer = release_date_trailer
        self.id_sutradara = id_sutradara
