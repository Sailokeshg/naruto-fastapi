'''This module contains classes mapped to database tables.'''
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import String

from init_db import Base

class Episode(Base):
    '''This class represents the episodes table.'''
    __tablename__ = 'naruto_ratings_data'

    episode_number_overall = Column(Integer, primary_key=True)
    season = Column(Integer)
    episode_number_in_season = Column(Integer)
    title = Column(String)
    directed_by = Column(String)
    written_by = Column(String)
    original_air_date = Column(DateTime)
    english_air_date = Column(DateTime)
    rating = Column(Float)
    votes = Column(Integer)
    description = Column(String)
    type = Column(String)

class Quotes(Base):
    '''This class represents the quotes table.'''
    __tablename__ = 'quotes'

    quote_id = Column(Integer, primary_key=True)
    character = Column(String)
    quote = Column(String)
