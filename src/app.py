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
        page: int = None

):
    para_dict = locals().copy()
    del para_dict['page']
    for i in list(para_dict.keys()):
        if para_dict[i] is None:
            del para_dict[i]

    all_passages = db_handler.query_passage(**para_dict)

    return all_passages[10 * (page - 1): 10 * page], len(all_passages)


@app.get('/heat/')
def query_heat(
        name=None
):
    years = [2018, 2019, 2020]
    quarters = [1, 2, 3, 4]
    heats = []
    print(name)
    for y in years:
        for q in quarters:
            heats.append(db_handler.query_topic(name=name, year=y, quarter=q)[0].heat)
    return heats