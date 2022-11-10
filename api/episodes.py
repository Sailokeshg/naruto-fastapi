from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from init_db import get_postgres_db
from services.episodes import get_complete_episode_details


router = APIRouter(prefix='/episodes')

@router.get('/all')
async def get_all_episode_details(session: Session = Depends(get_postgres_db)):
    episode_details = await get_complete_episode_details(session)
    return episode_details
