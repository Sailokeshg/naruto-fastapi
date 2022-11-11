"""This module contains application's core object"""
from fastapi import FastAPI

from api.episodes import router as episodes_router
from api.quotes import router as quotes_router
from api.ratings import router as ratings_router
from api.seasons import router as seasons_router


app = FastAPI(title="Naruto-API's",
              version="0.0.1",
              contact={
                  "name": "Sai Lokesh Reddy",
                  "url": "https://sailokeshg.github.io/myportfolio/",
                  "email": "sailokeshreddyg@gmail.com",
              },)

app.include_router(episodes_router, tags=['Episodes'])
app.include_router(seasons_router, tags=['Seasons'])
app.include_router(ratings_router, tags=['Ratings'])
app.include_router(quotes_router, tags=['Quotes'])


@app.get('/')
async def root():
    '''Denotes root of the application'''
    return {'status': 'OK'}
