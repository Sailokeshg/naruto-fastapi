"""This module contains apis related to episodes."""
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from init_db import get_postgres_db
from schemas.schemas import EpisodeType
from services.episodes import get_complete_episode_details
from services.episodes import get_complete_episode_details_by_id
from services.episodes import get_complete_episode_details_by_limit_and_offset
from services.episodes import get_complete_episode_details_by_type

router = APIRouter(prefix='/episodes')

@router.get('/all')
async def get_all_episode_details(session: Session = Depends(get_postgres_db)):
    '''Get all episode details'''
    episode_details = await get_complete_episode_details(session)
    return episode_details

@router.get('/{episode_number}')
async def get_episode_details(episode_number: int, session: Session = Depends(get_postgres_db)):
    '''Get episode details by episode number'''
    episode_details = await get_complete_episode_details_by_id(session, episode_number)
    return episode_details

@router.get('/types/{episode_type}')
async def get_episode_details_by_type(
        episode_type: EpisodeType, session: Session = Depends(get_postgres_db)):
    '''Get all episodes of a particular type'''
    episode_details = await get_complete_episode_details_by_type(episode_type, session)
    return episode_details

@router.get('/{limit}/{offset}')
async def get_episode_details_by_limit_and_offset(
        limit: int, offset: int, session: Session = Depends(get_postgres_db)):
    '''Get episode details by limit and offset.'''
    episode_details = await get_complete_episode_details_by_limit_and_offset(limit, offset, session)
    return episode_details
