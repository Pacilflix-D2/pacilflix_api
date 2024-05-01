from typing import Any
from psycopg2 import connect
from os import environ

from psycopg2._psycopg import connection


class Database:

    def __init__(self) -> None:
        self.db_name = environ.get('DB_NAME'),
        self.db_user = environ.get('DB_USER'),
        self.db_pass = environ.get('DB_PASS'),
        self.db_host = environ.get('DB_HOST'),
        self.db_port = environ.get('DB_PORT')

    # this could possibly throws error, so wrap this method with try catch
    def query(self, query: str) -> list[tuple[Any, ...]]:
        conn: connection = connect(
            dbname=self.db_name,
            user=self.db_user,
            password=self.db_pass,
            host=self.db_host,
            port=self.db_port
        )

        cursor = conn.cursor()
        cursor.execute(query)
        rows: list[tuple[Any, ...]] = cursor.fetchall()
        conn.close()

        return rows
