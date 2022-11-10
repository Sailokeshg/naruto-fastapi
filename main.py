from fastapi import FastAPI

from api.episodes import router as episodes_router
from api.quotes import router as quotes_router
from api.ratings import router as ratings_router
from api.seasons import router as seasons_router


app = FastAPI()

app.include_router(episodes_router, tags=['Episodes'])
app.include_router(seasons_router, tags=['Seasons'])
app.include_router(ratings_router, tags=['Ratings'])
app.include_router(quotes_router, tags=['Quotes'])


@app.get('/')
async def root():
    return {'status': 'OK'}
