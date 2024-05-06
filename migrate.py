from typing import Literal
from psycopg2 import connect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from dotenv import load_dotenv
from os import environ
import sys


def migrate():
    print('Migrating...')
    load_dotenv(override=True)

    connection = connect(
        dbname=environ.get('DB_NAME'),
        user=environ.get('DB_USER'),
        password=environ.get('DB_PASS'),
        host=environ.get('DB_HOST'),
        port=environ.get('DB_PORT', 5432)
    )
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    print('CONNECTION SUCCESS!')

    cursor = connection.cursor()
    with open('migration.sql', 'r') as sql_file:
        sql_commands = sql_file.read()

    cursor.execute(sql_commands)
    print('SUCCESS MIGRATE!')

    cursor.close()
    connection.close()


def seeding():
    print('Seeding...')
    load_dotenv(override=True)

    connection = connect(
        dbname=environ.get('DB_NAME'),
        user=environ.get('DB_USER'),
        password=environ.get('DB_PASS'),
        host=environ.get('DB_HOST'),
        port=environ.get('DB_PORT', 5432)
    )
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    print('CONNECTION SUCCESS!')

    cursor = connection.cursor()
    with open('seeds.sql', 'r') as sql_file:
        sql_commands = sql_file.read()

    cursor.execute(sql_commands)
    print('SUCCESS SEEDING!')

    cursor.close()
    connection.close()


def reset():
    print('Resetting DB...')
    load_dotenv(override=True)

    connection = connect(
        dbname=environ.get('DB_NAME'),
        user=environ.get('DB_USER'),
        password=environ.get('DB_PASS'),
        host=environ.get('DB_HOST'),
        port=environ.get('DB_PORT', 5432)
    )
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    print('CONNECTION SUCCESS!')

    cursor = connection.cursor()
    cursor.execute('DROP SCHEMA public CASCADE')
    print('Success drop schema!')
    cursor.execute('CREATE SCHEMA public')
    print('Success create schema!')

    cursor.close()
    connection.close()

    migrate()
    seeding()


if __name__ == '__main__':
    mode: Literal['MIGRATE', 'SEEDING', "RESET"] = 'MIGRATE'

    if len(sys.argv) != 1:
        arg1 = sys.argv[1]

        if arg1 == 'reset':
            mode = 'RESET'
        if arg1 == 'seed':
            mode = 'SEEDING'

    if mode == 'MIGRATE':
        migrate()
    elif mode == 'SEEDING':
        seeding()
    elif mode == 'RESET':
        reset()
