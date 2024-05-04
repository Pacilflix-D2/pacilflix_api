from typing import Any
from os import environ
from django.db import connection


class Database:

    def __init__(self) -> None:
        self.db_name = environ.get('DB_NAME'),
        self.db_user = environ.get('DB_USER'),
        self.db_pass = environ.get('DB_PASS'),
        self.db_host = environ.get('DB_HOST'),
        self.db_port = environ.get('DB_PORT')

    # this could possibly throws error, so wrap this method with try catch
    def query(self, query: str) -> list[tuple[Any, ...]]:
        with connection.cursor() as cursor:
            cursor.execute(query)
            rows: list[tuple[Any, ...]] = cursor.fetchall()
            return rows
