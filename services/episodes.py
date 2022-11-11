"""This module contains service methods related to episodes apis."""
from sqlalchemy import select
from sqlalchemy.orm import Session

from models.models import Episode
from schemas.schemas import EpisodeType

async def get_complete_episode_details(session: Session):
    '''Get all episode details from database'''
    episode_details = session.execute(select(Episode).order_by(
        Episode.season, Episode.episode_number_in_season)).all()
    if not episode_details:
        return {'error': 'No episode found for this id'}
    return episode_details

async def get_complete_episode_details_by_id(session: Session, episode_number: int):
    '''Get all episode details by its number from database'''
    details_by_id = session.query(Episode).get(episode_number)
    if not details_by_id:
        return {'error': 'No episode found for this id'}
    return details_by_id

async def get_complete_episode_details_by_type(episode_type: EpisodeType, session: Session):
    '''Get all episode details by its type from database'''
    details_by_type = session.query(Episode).filter(
        Episode.type == episode_type).order_by(
        Episode.season, Episode.episode_number_in_season).all()
    if not details_by_type:
        return {'error': 'No episode found for this type'}
    return details_by_type

async def get_complete_episode_details_by_limit_and_offset(
        limit: int, offset: int, session: Session):
    '''Get all episode details by its limit and offset from database'''
    details_by_limit_and_offset = session.query(Episode).limit(limit).offset(offset).all()
    if not details_by_limit_and_offset:
        return {'error': 'No episode found for this limit and offset'}
    return details_by_limit_and_offset
