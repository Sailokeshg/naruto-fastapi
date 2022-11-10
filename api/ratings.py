from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from init_db import get_postgres_db
from services.ratings import get_episode_details_greater_than_rating


router = APIRouter(prefix='/ratings')

@router.get('/{minimum_rating}')
async def get_all_episode_details(rating: float, session: Session = Depends(get_postgres_db)):
    episode_details = await get_episode_details_greater_than_rating(rating, session)
    return episode_details
