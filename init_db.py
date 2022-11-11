"""This module contains code related to databse connection"""
import os

import dotenv
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

dotenv.load_dotenv()

POSTGRES_URL = f'postgresql+psycopg2://{os.getenv("DB_USER")}:{os.getenv("PASSWORD")}@{os.getenv("HOST")}/{os.getenv("NAME")}'

postgres_engine = sqlalchemy.create_engine(POSTGRES_URL)
PostgresSession = sessionmaker(autocommit=False, autoflush=False, bind=postgres_engine)
PostgresSession.configure(bind=postgres_engine)

Base = declarative_base()

def get_postgres_db():
    '''Get a session for the postgres database'''
    database = None
    try:
        database = PostgresSession()
        yield database
    finally:
        database.close()


def create_session(schema, url):
    '''Create a session for a particular schema'''
    engine = sqlalchemy.create_engine(url)
    engine.dialect.description_encoding = None
    session_maker = sessionmaker()
    session_maker.configure(bind=engine)
    session = session_maker()
    query = "SET search_path=" + schema
    session.execute(query)
    return session
