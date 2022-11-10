from sqlalchemy import select

from models.models import Episode

async def get_complete_episode_details(session):
    episode_details = session.execute(select(Episode)).all()
    if not episode_details:
        return {'error': 'No episode found for this id'}
    return episode_details

async def get_complete_episode_details_by_id(session, episode_number):
    details_by_id = session.query(Episode).get(episode_number)
    if not details_by_id:
        return {'error': 'No episode found for this id'}
    return details_by_id
