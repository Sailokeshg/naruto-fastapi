from sqlalchemy import select

from models.models import Episode

async def get_complete_episode_details(session):
    details_by_id = session.execute(select(Episode)).all()
    return details_by_id
