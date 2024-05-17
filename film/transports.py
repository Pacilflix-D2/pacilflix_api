from dataclasses import dataclass
from typing import TypedDict


class FilmDict(TypedDict):
    ...


@dataclass
class FilmListResponse:
    films: list[FilmDict]
