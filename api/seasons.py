from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from init_db import get_postgres_db
from services.seasons import get_complete_episode_details_by_season_id
from services.seasons import get_complete_episode_details_by_season_number_and_episode_number


router = APIRouter(prefix='/seasons')

@router.get('/{season_number}',
            description="This endpoint returns all the episodes list of a season.")
async def get_episode_details_by_season_number(season_number: int, session: Session = Depends(get_postgres_db)):
    '''Get all episode details by season number'''
    episode_details = await get_complete_episode_details_by_season_id(session, season_number)
    return episode_details

@router.get('/{season_number}/{episode_number}',
            description="This endpoint returns the details of a particular episode.")
async def get_episode_details_by_its_season_specific_episode_number(season_number: int, episode_number: int, session: Session = Depends(get_postgres_db)):
    '''Get episode details by season specific episode number'''
    episode_details = await get_complete_episode_details_by_season_number_and_episode_number(session, season_number, episode_number)

    return episode_details
