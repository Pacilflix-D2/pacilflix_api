from core.models.episode import Episode
from core.repositories.database import Database


class EpisodeRepository(Database):
    def find_all(self) -> list[Episode]:
        ...

    def find_by_pk(self, id_series: str, sub_judul: str) -> Episode:
        ...
