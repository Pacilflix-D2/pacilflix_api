from dataclasses import dataclass

from core.models.film import Film


@dataclass
class FilmListResponse:
    films: list[Film]
