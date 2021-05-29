import pickle
import os

from tqdm import tqdm

from src import settings
from src.database.db_handler import DBHandler
from src.database.models import Passage, Topic

handler = DBHandler(settings.DBHandler.engine)

passages = handler.query_passage()
session = handler.session
topics = session.query(Topic).filter_by()

for i in tqdm(topics):
    for j in passages:
        if int(j.topic) == i.topic_id and j.pic_url is not None:
            i.pic_url = j.pic_url
            break

session.commit()
session.close()
