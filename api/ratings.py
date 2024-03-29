"""This module contains apis related to ratings."""
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from init_db import get_postgres_db
from services.ratings import get_episode_details_greater_than_rating

router = APIRouter(prefix='/ratings')

@router.get('/{minimum_rating}',
            description="This endpoint returns the episodes with rating greater than the minimum rating.")
async def get_all_episode_details_with_rating_greater_than_requested_rating(rating: float, session: Session = Depends(get_postgres_db)):
    '''Get all episode details with rating greater than requested rating'''
    episode_details = await get_episode_details_greater_than_rating(rating, session)
    return episode_details
