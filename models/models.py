from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import String

from init_db import Base

class Episode(Base):
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
