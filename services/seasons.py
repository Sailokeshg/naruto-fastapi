from models.models import Episode

async def get_complete_episode_details_by_season_id(session, season_number):
    details_by_season_id = session.query(Episode).filter_by(season=season_number).all()
    if details_by_season_id == [] or (details_by_season_id is None):
        return {'error': 'No episode found for this season'}
    return details_by_season_id
