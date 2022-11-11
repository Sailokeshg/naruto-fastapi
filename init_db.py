import os

import dotenv
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

dotenv.load_dotenv()

POSTGRES_DATABASE_URL = f'postgresql+psycopg2://{os.getenv("USER")}:{os.getenv("PASSWORD")}@{os.getenv("HOST")}/{os.getenv("NAME")}'

postgres_engine = sqlalchemy.create_engine(POSTGRES_DATABASE_URL)
PostgresSession = sessionmaker(autocommit=False, autoflush=False, bind=postgres_engine)
PostgresSession.configure(bind=postgres_engine)

Base = declarative_base()

def get_postgres_db():
    db = None
    try:
        db = PostgresSession()
        yield db
    finally:
        db.close()


def create_session(schema, url):
    engine = sqlalchemy.create_engine(url)
    engine.dialect.description_encoding = None
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    metadata = sqlalchemy.MetaData(bind=session.bind)
    query = "SET search_path=" + schema
    session.execute(query)
    return session
