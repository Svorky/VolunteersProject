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
        
def update(table_name, col_to_change, col_where, params):
    with psycopg2.connect(
        dbname=DBNAME, user=USER, password=PASSWORD, host=HOST, port=PORT
    ) as connection:
        cursor = connection.cursor()

        query = f'''UPDATE {table_name} SET {col_to_change}=%s
        WHERE {col_where}=%s'''
        cursor.execute(
            query,
            params
        )
        
        connection.commit()
        
def select_volunteer(where={}):
    result = []
    with psycopg2.connect(
        dbname=DBNAME, user=USER, password=PASSWORD, host=HOST, port=PORT
    ) as connection:

        cursor = connection.cursor(cursor_factory = psycopg2.extras.RealDictCursor)

        where_query_raw = []
        for key in where:
            s = f"{key}"
            where_query_raw.append(s)
        
        where_query = ",\n".join(where_query_raw)

        query = f'''
                      SELECT
	volunteer.id,
	volunteer.name as volunteer_name,
	volunteer.birth_date,
	city.name as city,
	volunteer.telephone,
	language.name as language,
	volunteer.has_driver_licence,
	volunteer.has_car,
	car.name as car,
	volunteer.love_animals,
	animal.name as animal
FROM
	city
	INNER JOIN volunteer
	 ON city.id = volunteer.city_id
	LEFT OUTER JOIN volunteer_language
	 ON volunteer.id = volunteer_language.volunteer_id
	LEFT OUTER JOIN volunteer_car
	 ON volunteer.id = volunteer_car.volunteer_id
	LEFT OUTER JOIN volunteer_animal
	 ON volunteer.id = volunteer_animal.volunteer_id
	LEFT OUTER JOIN animal
	 ON volunteer_animal.animal_id = animal.id
	LEFT OUTER JOIN car
	 ON volunteer_car.car_id = car.id
	LEFT OUTER JOIN language
	 ON volunteer_language.language_id = language.id
WHERE
    {where_query}
                      '''
        cursor.execute(
            query,
            list(where.values())
        )

        result = cursor.fetchall()

    return result