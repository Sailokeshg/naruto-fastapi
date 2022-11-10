from fastapi import FastAPI

from api.episodes import router as episodes_router
from api.seasons import router as seasons_router
app = FastAPI()

app.include_router(episodes_router, tags=['Episodes'])
app.include_router(seasons_router, tags=['Seasons'])


@app.get('/')
async def root():
    return {'status': 'OK'}
