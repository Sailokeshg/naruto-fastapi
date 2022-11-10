from fastapi import FastAPI

from api.episodes import router

app = FastAPI()

app.include_router(router, tags=['Episodes'])

@app.get('/')
async def root():
    return {'status': 'OK'}
