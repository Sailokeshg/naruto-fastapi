import logging

from fastapi import FastAPI


# TO DO   : to restrict another library logger to print something in our console
# get logger named as 'filename' and it will use the handler of root logger
logger = logging.getLogger(__name__)


app = FastAPI()


@app.get('/')
async def root():
    return {'status': 'OK'}
