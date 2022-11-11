"""This module contains service methods related to quotes apis."""
from sqlalchemy.orm import Session

from models.models import Quotes
from schemas.schemas import Characters

async def get_all_quotes_details(session: Session):
    '''Get all quotes details from database'''
    all_quotes = session.query(Quotes).all()

    return all_quotes

async def get_quote_details_by_id(session: Session, quote_id: int):
    '''Get all quotes details by its number from database'''
    quote_details = session.query(Quotes).get(quote_id)
    return quote_details

async def get_quote_details_by_limit_and_offset_values(limit: int, offset: int, session: Session):
    '''Get all quotes details by its limit and offset from database'''
    quote_details = session.query(Quotes).limit(limit).offset(offset).all()
    return quote_details

async def get_available_character_names_for_quotes(session: Session):
    '''Get all the character names for which quotes are available'''
    quote_details = session.query(Quotes.character).distinct().all()
    return quote_details

async def get_quote_details_of_a_character_name(character_name: Characters, session: Session):
    '''Get all the quotes said by a particular character'''
    quote_details = session.query(Quotes).filter(Quotes.character == character_name).all()
    return quote_details
