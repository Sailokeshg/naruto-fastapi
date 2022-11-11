"""This module contains apis related to quotes."""
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from init_db import get_postgres_db
from schemas.schemas import Characters
from services.quotes import get_all_quotes_details
from services.quotes import get_available_character_names_for_quotes
from services.quotes import get_quote_details_of_a_character_name

router = APIRouter(prefix='/quotes')


@router.get('/all', description="This endpoint returns all the quotes with their details.")
async def get_all_quotes(session: Session = Depends(get_postgres_db)):
    '''Get all quotes details'''
    all_quotes = await get_all_quotes_details(session)
    return all_quotes


@router.get('/characters', description="This endpoint returns the details of a particular quote.")
async def get_characters_details(session: Session = Depends(get_postgres_db)) -> list:
    '''Get all the character names for which quotes are available'''
    quote_details = await get_available_character_names_for_quotes(session)
    return quote_details

@router.get('/character/{chatacter_name}',
            description="This endpoint returns the details of a particular quote of the character.")
async def get_quote_details_by_character_name(chatacter_name: Characters, session: Session = Depends(get_postgres_db)):
    '''Get all the quotes said by a particular character'''
    quote_details = await get_quote_details_of_a_character_name(chatacter_name, session)
    return quote_details
