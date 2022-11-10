from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from init_db import get_postgres_db
from services.episodes import get_complete_episode_details
from services.episodes import get_complete_episode_details_by_id


router = APIRouter(prefix='/episodes')

@router.get('/all')
async def get_all_episode_details(session: Session = Depends(get_postgres_db)):
    episode_details = await get_complete_episode_details(session)
    return episode_details

@router.get('/{episode_number}')
async def get_episode_details(episode_number: int, session: Session = Depends(get_postgres_db)):
    episode_details = await get_complete_episode_details_by_id(session, episode_number)
    return episode_details
