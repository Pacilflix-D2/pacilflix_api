from core.models.base import BaseModel


class Series(BaseModel):
    def __init__(self, id_tayangan: str) -> None:
        self.id_tayangan = id_tayangan
