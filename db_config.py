# db_config.py

import psycopg2

def create_connection():
    try:
        connection = psycopg2.connect(
            host="localhost",
            port="5432",
            user="postgres",
            password="23.02.2005",
            database="project4"
        )
        return connection
    except psycopg2.Error as e:
        print(f"Помилка підключення: {e}")
        return None
