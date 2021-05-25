from typing import List

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src import settings
from src.api.models import Topic, Passage
from src.database import DBHandler
from src.utils import trans_model

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.App.CORS.origins,
    allow_credentials=settings.App.CORS.credentials,
    allow_methods=settings.App.CORS.methods,
    allow_headers=settings.App.CORS.headers,
)
db_handler = DBHandler(settings.DBHandler.engine)


@app.get('/topic/')
def query_topics(
        id=None,
        name=None,
        year=None,
        quarter=None,
        heat=None,
        p_num=None,
        abstract=None,
        pic_url=None,
        source=None
):
    para_dict = locals()
    for i in list(para_dict.keys()):
        if para_dict[i] is None:
            del para_dict[i]

    return db_handler.query_topic(**para_dict)


@app.get('/passage/')
def query_passages(
        id=None,
        title=None,
        data=None,
        content=None,
        abstract=None,
        website=None,
        url=None,
        topic=None,
        source=None
):
    para_dict = locals()
    for i in list(para_dict.keys()):
        if para_dict[i] is None:
            del para_dict[i]

    return db_handler.query_passage(**para_dict)
