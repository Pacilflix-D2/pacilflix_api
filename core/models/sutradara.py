from core.models.base import BaseModel


class Contributor(BaseModel):
    def __init__(self, _id: str) -> None:
        self.id = _id
