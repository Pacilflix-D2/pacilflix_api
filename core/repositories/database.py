from typing import Any
from os import environ
from django.db import connection


class Database:

    def __init__(self) -> None:
        self._db_name = environ.get('DB_NAME'),
        self._db_user = environ.get('DB_USER'),
        self._db_pass = environ.get('DB_PASS'),
        self._db_host = environ.get('DB_HOST'),
        self._db_port = environ.get('DB_PORT')

    # this could possibly throws error, so wrap this method with try catch
    def select(self, query: str) -> list[tuple[Any, ...]]:
        with connection.cursor() as cursor:
            cursor.execute(query)
            rows: list[tuple[Any, ...]] = cursor.fetchall()
            return rows

    def insert(self, query: str) -> None:
        with connection.cursor() as cursor:
            cursor.execute(query)
