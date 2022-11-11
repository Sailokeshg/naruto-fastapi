"""This module contains service methods related to ratings apis."""
from sqlalchemy.orm import Session

from models.models import Episode

async def get_episode_details_greater_than_rating(rating: float, session: Session):
    '''Get all episode details with rating greater than requested rating'''
    episode_details = session.query(Episode).filter(Episode.rating > rating).all()
    if not episode_details:
        return {'error': 'No episode found for this id'}
    return episode_details
