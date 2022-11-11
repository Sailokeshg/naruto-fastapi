"""This module contains service methods related to seasons apis."""
from models.models import Episode

async def get_complete_episode_details_by_season_id(session, season_number):
    '''Get all episode details by its season number from database'''
    details_by_season_id = session.query(Episode).filter_by(
        season=season_number).order_by(
        Episode.season, Episode.episode_number_in_season).all()
    if details_by_season_id == [] or (details_by_season_id is None):
        return {'error': 'No episode found for this season'}
    return details_by_season_id

async def get_complete_episode_details_by_season_number_and_episode_number(
        session, season_number, episode_number):
    '''Get all episode details by its season number and episode number from database'''
    details_by_season_id = session.query(Episode).filter_by(
        season=season_number, episode_number_in_season=episode_number).all()
    if details_by_season_id == [] or (details_by_season_id is None):
        return {'error': 'No episode found for this season'}
    return details_by_season_id
