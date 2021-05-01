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


@app.get('/')
def root():
    return 'see docs at: http://127.0.0.1:8000/docs'


@app.get('/topic/', response_model=List[Topic])
def query_topics(source: str = None, year: int = None, quarter: int = None):
    kwargs = dict()
    if source:
        kwargs['source'] = source
    if year:
        kwargs['year'] = year
    if quarter:
        kwargs['quarter'] = quarter
    return list(
        map(
            trans_model, db_handler.query_topic(**kwargs)
        )
    )


@app.get('/passage/', response_model=List[Passage])
def query_passages(topic: str = None):
    kwargs = dict()
    if topic:
        kwargs['topic'] = topic
    return list(
        map(
            trans_model, db_handler.query_passage(**kwargs)
        )
    )
