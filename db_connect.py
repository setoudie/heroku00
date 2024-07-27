"""
    In this file we define a function who create a connection with the database
"""
from urllib.parse import urlparse
import psycopg2

# This is a Heroku database for my first severless project
HEROKU_DATABASE_URL = ("postgres://ue8vh0mnffvauq:p919e0f98c49f44fc6a9790af2b870a008cbb66de372be8a51c460f6a492b519e"
                       "@caij57unh724n3.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/ddi27h5fhgqasi")

parsed_url = urlparse(HEROKU_DATABASE_URL)
# print(parsed_url.path)
DB_NAME = parsed_url.path[1:]
USER = parsed_url.username
PASSWORD = parsed_url.password
HOST = parsed_url.hostname
PORT = parsed_url.port


def get_db_connection():
    db = psycopg2.connect(
        database=DB_NAME,
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT
    )
    return db
