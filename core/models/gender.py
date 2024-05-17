from core.models.base import BaseModel


class Genre(BaseModel):
    def __init__(self, id_tayangan: str, genre: str) -> None:
        self.id_tayangan = id_tayangan
        self.genre = genre
