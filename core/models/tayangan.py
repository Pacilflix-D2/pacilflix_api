from datetime import date
from typing import Literal
from core.models.base import BaseModel
from core.models.episode import Episode
from core.models.riwayat_nonton import RiwayatNonton
from core.repositories.episode import EpisodeRepository
from core.repositories.film import FilmRepository
from core.repositories.riwayat_nonton import RiwayatNontonRepository
from core.repositories.ulasan import UlasanRepository
from core.utils.exceptions.internal_server_error import InternalServerException


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

    def get_type(self) -> Literal['FILM', 'SERIES']:
        try:
            FilmRepository().find_by_id(id_tayangan=self.id)
            return 'FILM'
        except:
            return 'SERIES'

    def _base_count_total_views(self, watch_histories: list[RiwayatNonton]) -> int:
        total_views = 0
        for watch_history in watch_histories:
            watch_time_in_minutes = (watch_history.end_date_time -
                                     watch_history.start_date_time).total_seconds() / 60
            total_duration = self.get_total_duration()

            if watch_time_in_minutes > total_duration:
                raise InternalServerException(
                    'Lama menonton tidak dapat melebihi durasi film.')

            watch_time_percentage = (
                watch_time_in_minutes / total_duration) * 100
            if watch_time_percentage >= 70:
                total_views += 1

        return total_views

    def get_total_views(self) -> int:
        watch_histories: list[RiwayatNonton] = RiwayatNontonRepository(
        ).find_by_id_tayangan(id_tayangan=self.id)

        return self._base_count_total_views(watch_histories=watch_histories)

    def get_total_views_last_week(self) -> int:
        watch_histories: list[RiwayatNonton] = RiwayatNontonRepository(
        ).find_by_id_tayangan_last_week(id_tayangan=self.id)

        return self._base_count_total_views(watch_histories=watch_histories)

    def get_total_duration(self) -> int:
        if self.get_type() == 'FILM':
            return FilmRepository().find_by_id(id_tayangan=self.id).durasi_film
        else:
            total_duration = 0
            episodes: list[Episode] = EpisodeRepository(
            ).find_by_id_series(id_series=self.id)

            for episode in episodes:
                total_duration += episode.durasi

            return total_duration

    def _get_rating_avg_film(self) -> float:
        reviews = UlasanRepository().find_by_id_tayangan(id_tayangan=self.id)
        rating_sum = 0
        for review in reviews:
            rating_sum += review.rating

        return rating_sum / len(reviews)

    def _get_rating_avg_series(self) -> float:
        reviews = UlasanRepository().find_by_id_tayangan(id_tayangan=self.id)
        rating_sum = 0
        for review in reviews:
            rating_sum += review.rating

        return rating_sum / len(reviews)

    def get_rating(self) -> float:
        if self.get_type() == 'FILM':
            return self._get_rating_avg_film()
        else:
            return self._get_rating_avg_series()
