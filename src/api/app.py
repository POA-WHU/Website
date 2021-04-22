from fastapi import FastAPI

import settings
from api.models import Topic, Passage
from database import DBHandler
from utils import trans_model

app = FastAPI()
db_handler = DBHandler(settings.DBHandler.engine)


@app.get('/')
def root():
    return 'see docs at: http://127.0.0.1:8000/docs'


@app.get('/topic/', response_model=list[Topic])
def query_topics(source: str, year: int, quarter: int):
    return list(
        map(
            trans_model, db_handler.query_topic(source, year, quarter)
        )
    )


@app.get('/passage/', response_model=list[Passage])
def query_passages(topic: str):
    return list(
        map(
            trans_model, db_handler.query_passage(topic)
        )
    )
