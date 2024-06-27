import psycopg2
import psycopg2.extras
import os
from dotenv import load_dotenv

load_dotenv()

DBNAME = os.getenv("DBNAME")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")


def select(query, params=[]) -> list[psycopg2.extras.RealDictRow]:
    result = []
    with psycopg2.connect(
        dbname=DBNAME, user=USER, password=PASSWORD, host=HOST, port=PORT
    ) as connection:

        cursor = connection.cursor(cursor_factory = psycopg2.extras.RealDictCursor)

        cursor.execute(
            query,
            params
        )

        result = cursor.fetchall()

    return result

def insert(query, params, return_id = True) -> int | None:
    if return_id:
        query = query + " RETURNING id;"
    id = None
    with psycopg2.connect(
        dbname=DBNAME, user=USER, password=PASSWORD, host=HOST, port=PORT
    ) as connection:

        cursor = connection.cursor()

        cursor.execute(
            query,
            params
        )

        connection.commit()
        
        if return_id:
            id = cursor.fetchone()[0]
    return id

def delete(query, params):
    with psycopg2.connect(
        dbname=DBNAME, user=USER, password=PASSWORD, host=HOST, port=PORT
    ) as connection:
        cursor = connection.cursor()

        cursor.execute(
            query,
            params
        )
        
        connection.commit()