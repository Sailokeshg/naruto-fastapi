from sqlalchemy.orm import Session

from models.models import Quotes
from schemas.schemas import Characters

async def get_all_quotes_details(session: Session):
    all_quotes = session.query(Quotes).all()

    return all_quotes

async def get_quote_details_by_id(session: Session, quote_id: int):
    quote_details = session.query(Quotes).get(quote_id)
    return quote_details

async def get_quote_details_by_limit_and_offset_values(limit: int, offset: int, session: Session):
    quote_details = session.query(Quotes).limit(limit).offset(offset).all()
    return quote_details

async def get_available_character_names_for_quotes(session: Session):
    quote_details = session.query(Quotes.character).distinct().all()
    return quote_details

async def get_quote_details_of_a_character_name(character_name: Characters, session: Session):
    quote_details = session.query(Quotes).filter(Quotes.character == character_name).all()
    return quote_details
