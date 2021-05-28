from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src import settings
from src.database import DBHandler

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
        source=None,
        page: int = None
):
    para_dict = locals()
    del para_dict['page']
    for i in list(para_dict.keys()):
        if para_dict[i] is None:
            del para_dict[i]

    all_topics = db_handler.query_topic(**para_dict)
    all_topics = sorted(all_topics, key=lambda x: x.heat, reverse=True)
    return all_topics[10 * (page - 1): 10 * page], len(all_topics)


@app.get('/passage/')
def query_passages(
        id=None,
        title=None,
        date=None,
        content=None,
        abstract=None,
        website=None,
        url=None,
        topic=None,
        source=None,
        year: int = None,
        quarter: int = None,
        page: int = None

):
    para_dict = locals().copy()
    del para_dict['page']
    for i in list(para_dict.keys()):
        if para_dict[i] is None:
            del para_dict[i]

    all_passages = db_handler.query_passage(**para_dict)
    all_passages = sorted(all_passages, key=lambda x: x.date, reverse=True)
    return all_passages[10 * (page - 1): 10 * page], len(all_passages)


@app.get('/heat/')
def query_heat(
        topic_id: int
):
    years = [2018, 2019, 2020]
    quarters = [1, 2, 3, 4]
    heats_and_names = []
    for y in years:
        for q in quarters:
            try:
                topic = db_handler.query_topic(topic_id=topic_id, year=y, quarter=q)[0]
                heats_and_names.append((topic.heat, topic.name))
            except IndexError:
                heats_and_names.append((0, ''))
    return heats_and_names
